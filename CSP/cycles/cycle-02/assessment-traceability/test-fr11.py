"""Verify the supplementary FR11 trace on synthetic records."""
from pathlib import Path

from rdflib import Graph, Namespace

FOLDER = Path(__file__).resolve().parent
CASE = Namespace("urn:csp:cycle2:fr11:")
K = Namespace("http://purl.org/ontoksd#")
DCT = Namespace("http://purl.org/dc/terms/")
QUERY = (FOLDER / "fr11-trace.rq").read_text(encoding="utf-8")


def check(label, expected, remove=None, add=None):
    graph = Graph().parse(FOLDER / "fr11-fixture.ttl")
    if remove is not None:
        graph.remove(remove)
    if add is not None:
        graph.add(add)
    rows = list(graph.query(QUERY))
    assert [(r.judgment, r.occasion) for r in rows] == expected, (label, rows)
    assert all(r.learner == CASE.learner and r.target == CASE.target
               and r.criterion == CASE.criterion and r.item for r in rows), label
    print(f"PASS {label}: {len(rows)} trace(s)")


first = (CASE.j1, CASE.o1)
second = (CASE.j2, CASE.o2)
check("two distinct occasions", [first, second])
check("missing criterion", [first], remove=(CASE.j2, DCT.references, CASE.criterion))
check("criterion from another assessment", [first],
      remove=(CASE.j2, DCT.references, CASE.criterion),
      add=(CASE.j2, DCT.references, CASE.otherCriterion))
check("cross-occasion evidence", [first],
      remove=(CASE.j2, K.supportedByEvidence, CASE.e2),
      add=(CASE.j2, K.supportedByEvidence, CASE.e1))
check("mixed evidence origins", [first],
      add=(CASE.j2, K.supportedByEvidence, CASE.e1))
check("learner mismatch", [first],
      remove=(CASE.p2, K.hasLearner, CASE.learner),
      add=(CASE.p2, K.hasLearner, CASE.otherLearner))
