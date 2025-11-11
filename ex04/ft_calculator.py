class calculator:
    """Minimum matrix calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Return the dot product of two vectors."""
        ret = 0
        for i in range(len(V1)):
            ret += V1[i] * V2[i]
        print(f"Dot product is: {ret}")
        return ret

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Return the element-wise sum of two vectors."""
        ret: list[float] = []
        for i in range(len(V1)):
            ret.append(float(V1[i]) + V2[i])
        print(f"Add Vector is : {ret}")
        return ret

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Return the element-wise difference of two vectors."""
        ret: list[float] = []
        for i in range(len(V1)):
            ret.append(float(V1[i]) - V2[i])
        print(f"Sous Vector is : {ret}")
        return ret
