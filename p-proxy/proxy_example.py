class College(object):
    def studyingInCollege(self):
        print("Studying In College...")


class CollegeProxy(object):
    def __init__(self):
        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):
        print(
            "Proxy in action. Checking to see if the balance of student is clear or not..."
        )

        if self.feeBalance <= 500:
            self.college = College()
            self.college.studyingInCollege()
        else:
            print("Your fee balance is greater than 500, first pay the fee")


if __name__ == "__main__":
    collegeProxy = CollegeProxy()

    collegeProxy.studyingInCollege()

    collegeProxy.feeBalance = 100

    collegeProxy.studyingInCollege()
