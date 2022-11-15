#   210. Course Schedule II


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        
        noPreCourses = [n for n in range(numCourses) if not courses[n]]
        count = []
        while noPreCourses:
            noPre = noPreCourses.pop()
            count.append(noPre)
            for course in pres[noPre]:
                courses[course].remove(noPre)
                if not courses[course]:
                    noPreCourses.append(course)
        return count if len(count) == numCourses else []
