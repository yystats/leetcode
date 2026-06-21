# print org chart 
# employee = 
# [["8","8","Alice"],["2","8","Bob"],["3","2","Charlie"],["4","3","David"],["5","4","Eva"],["6","3","Frank"],["7","8","Grace"]]


class printOrgChart:
    def __init__(self) -> None:
        self.manager_to_report = {}
        self.id_to_name = {}
        self.ceo_id = None

    def create_org_chart(self, employees):
        for emp_id, mgr_id, name in employees:
            self.id_to_name[emp_id] = name

            if emp_id == mgr_id:
                self.ceo_id = emp_id
            else:
                if mgr_id not in self.manager_to_report:
                    self.manager_to_report[mgr_id] = []
                self.manager_to_report[mgr_id].append(emp_id)
        
    def get_org_string(self):
        output = []

        def dfs(current_id, depth):
            indent = '-' * (4 * depth)
            output.append(f"{indent} {self.id_to_name[current_id]}")

            if current_id in self.manager_to_report:
                for report_id in self.manager_to_report[current_id]:
                    dfs(report_id, depth + 1)

        dfs(self.ceo_id, 0)
        return '\n'.join(output)


employees = [["8","8","Alice"],["2","8","Bob"],["3","2","Charlie"],["4","3","David"],["5","4","Eva"],["6","3","Frank"],["7","8","Grace"]]
p = printOrgChart()
p.create_org_chart(employees)
print(p.get_org_string())


