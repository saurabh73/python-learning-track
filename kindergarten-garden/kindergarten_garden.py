class Garden:

    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.garden = [list(s) for s in diagram.splitlines()]
        self.students = [student.lower() for student in students]
        self.students.sort()
        self.plant_values = dict({
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets',
    })

    def plants(self, student):
        index = self.students.index(student.lower())
        ans = []
        for i in range(0,2):
            for j in range(0,2):
                ans.append(self.plant_values[self.garden[i][2*index + j]])
        return ans
