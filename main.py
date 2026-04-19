from artifact import Artifact, Painting, Sculpture, give_name_artifact
from renaissance import painting, sculpture, building

def give_name_main():
    return f"main name: {__name__}"


if __name__ == "__main__":
    a1 = Artifact("a1", 1598)
    a2 = Artifact("a2", 1958)
    a3 = Artifact("a3", 1002)

    p1 = Painting("p1", 1587, "art1", "oil")
    p2 = Painting("p2", 902, "art2", "pastel")
    p3 = Painting("p3", 1877, "art3", "crayon")

    s1 = Sculpture("s1", 1950, "marble", 15)
    s2 = Sculpture("s2", 1801, "bronze", 100)

    print(f"{s1.is_old(10)=}")
    print(give_name_artifact())
    print(give_name_main())
    print(__name__)
    print(painting)
    print(sculpture)
    print(building)