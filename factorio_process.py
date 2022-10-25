import math


class FormalVector:
    _ZERO = "FormalVector.zero()"
    _registry = {}

    @classmethod
    def named(cls, name, content=None):
        if name not in cls._registry:
            cls._registry[name] = cls(
                components={name: 1},
                basis={name: content},
                name=name,
            )
        return cls._registry[name]

    @classmethod
    def zero(cls):
        name = cls._ZERO
        if name not in cls._registry:
            cls._registry[name] = cls(
                components={},
                basis={},
                name=name,
            )
        return cls._registry[name]

    @classmethod
    def sum(cls, vectors):
        return sum(vectors, start=cls.zero())

    def __init__(self, components=None, basis=None, name=None):
        self.name = name
        self.components = components
        self.basis = basis
        if self.components.keys() != self.basis.keys():
            raise ValueError(
                f"Component keys and basis keys do not match! "
                f"components={components.keys()}, basis={basis.keys()}"
            )

    def is_leaf(self):
        return self.components == {self.name: 1}

    @property
    def content(self):
        if self.is_leaf():
            return self.basis[self.name]
        else:
            return self

    def pairs(self):
        return [(self.components[k], self.basis[k]) for k in self.components]

    def triples(self):
        return [
            (k, self.components[k], self.basis[k]) for k in self.components
        ]

    def project(self, k):
        return self.components[k] * FormalVector.named(k, self.basis[k])

    def __getitem__(self, item):
        return self.components[item]

    def __add__(self, other):
        components = {}
        basis = {}
        keys = set(
            list(self.components.keys()) +
            list(other.components.keys())
        )
        for k in keys:
            components[k] = (
                self.components.get(k, 0) +
                other.components.get(k, 0)
            )
            basis[k] = self.basis.get(k) or other.basis.get(k)
        return FormalVector(components=components, basis=basis)

    def __rmul__(self, alpha):
        return FormalVector(
            components={k: alpha*v for (k, v) in self.components.items()},
            basis=self.basis,
        )

    def __sub__(self, other):
        return self + (-1) * other

    def __neg__(self):
        return (-1) * self

    def __repr__(self):
        if self.name:
            return self.name
        elif self.components == {}:
            return self._ZERO
        else:
            return " + ".join(
                f"{k}" if v == 1 else
                f"-{k}" if v == -1 else
                f"{v}*{k}"
                for (k, v) in self.components.items()
            )


class Process:

    def __init__(self, name, inputs, seconds, out_multiplier=1):
        self.name = name
        self.inputs = inputs
        self.seconds = seconds
        self.out_multiplier = out_multiplier

    def __repr__(self):
        return f"<Process: '{self.name}'>"

    def optimal_process_duplication(self, output_per_second):
        return self.seconds * output_per_second / self.out_multiplier

    def optimal_input_demands(self, output_per_second):
        return output_per_second / self.out_multiplier * self.inputs

    def input_demands_with_duplication(self, duplication):
        return duplication / self.seconds * self.inputs


def manufactured(name, inputs, seconds, out_multiplier=1):
    return FormalVector.named(
        name,
        Process(name, inputs, seconds, out_multiplier),
    )


def raw(name):
    return FormalVector.named(name)


def _optimize_leaf(process, demand, path):
    optimal_duplication = process.optimal_process_duplication(demand)
    optimal_demands = process.input_demands_with_duplication(optimal_duplication)

    basic_result = {
        "rate": demand,
        "process": path,
        "N": optimal_duplication,
        "demand": optimal_demands,
    }

    return {"processes": [basic_result], "raw_inputs": FormalVector.zero()}


def _join_optimize_results(results):
    results = list(results)
    processes = sum(
        [result["processes"] for result in results],
        start=[],
    )
    raw_inputs = FormalVector.sum(
        [result["raw_inputs"] for result in results],
    )
    return {"processes": processes, "raw_inputs": raw_inputs}


def optimize(process_demand, assume_raw=None, path=None):
    assume_raw = assume_raw or []

    # If our input is made of one thing, describe how to optimize its
    # manufacture
    if len(triples := process_demand.triples()) == 1:
        (name, demand, process) = triples[0]

        # Process is None means the input is raw, and no process produces it.
        # Tally it with the raw inputs.
        #
        # Also treat as raw those processes whose name appears in our list
        # `assume_raw`.
        if process is None or name in assume_raw:
            return {"processes": [], "raw_inputs": process_demand}

        # Otherwise it's a process we have to optimize.  Do so, then join that
        # to the optimized output for its constituent processes.
        else:
            path = path or [name]
            base = _optimize_leaf(process, demand, path)
            return _join_optimize_results(
                [
                    base,
                    optimize(
                        base["processes"][0]["demand"],
                        assume_raw=assume_raw,
                        path=path,
                    ),
                ]
            )

    # If our input is a combination of things, project out each component,
    # optimize each, and join the result
    else:
        path = path or []
        return _join_optimize_results(
            optimize(
                process_demand.project(k),
                assume_raw=assume_raw,
                path=path+[k],
            )
            for k in process_demand.components
        )


def format_optimize_result(opt, name=None):
    name = name or "Process"
    lines = [
        f"#### {name} ({opt['raw_inputs']}) ####",
    ]
    for process in opt["processes"]:
        path = " > ".join(process["process"])
        lines.append(
            f"{path}\n"
            f"    N = {process['N']}  ({math.ceil(process['N'])})\n"
            f"    {process['rate']}*{process['process'][-1]} = {process['demand']}"
        )
    return "\n".join(lines)
