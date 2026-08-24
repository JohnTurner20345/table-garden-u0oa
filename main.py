from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    project: str
    owner: str
    profile: str

def build_snapshot() -> Snapshot:
    return Snapshot("table-garden-u0oa", "JohnTurner20345", "0035")

if __name__ == "__main__":
    snapshot = build_snapshot()
    print(f"{snapshot.project}: {snapshot.owner}")
