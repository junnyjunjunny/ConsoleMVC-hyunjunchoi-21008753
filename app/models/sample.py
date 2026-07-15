from dataclasses import dataclass


@dataclass
class Sample:
    sample_id: str
    name: str
    avg_production_time: float
    yield_rate: float
    stock: int = 0


class SampleModel:
    """In-memory store for Sample entities. Owns data and invariants only."""

    def __init__(self):
        self._samples = {}

    def add(self, sample: Sample) -> None:
        if sample.sample_id in self._samples:
            raise ValueError(f"Sample already exists: {sample.sample_id}")
        self._samples[sample.sample_id] = sample

    def get(self, sample_id: str) -> Sample:
        if sample_id not in self._samples:
            raise KeyError(f"Sample not found: {sample_id}")
        return self._samples[sample_id]

    def list_all(self):
        return list(self._samples.values())

    def search_by_name(self, keyword: str):
        keyword = keyword.lower()
        return [s for s in self._samples.values() if keyword in s.name.lower()]
