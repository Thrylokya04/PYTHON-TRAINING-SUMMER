class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count=len(students)
        while(sandwiches and students and sandwiches[0] in students):
            if(sandwiches[0]!=students[0]):
                students.append(students[0])
                students.pop(0)
            else:
                students.pop(0)
                sandwiches.pop(0)
                count-=1
        return count
