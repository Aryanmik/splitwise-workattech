class GroupsDb:
    groups = {}

    def get(self, group_id):
        group = self.groups.get(group_id)
        if not group:
            print(f"Group : {group_id} not present in db")
        return group

    def save(self, group):
        self.groups[group.id] = group
        return group
