class PortfolioManager:
    def __init__(self, developer_name: str, major: str):
        self.developer_name = developer_name
        self.major = major
        self.projects = []
    def add_project(self, project_name: str, tech_stack: list[str]) -> None:
        project = {'name': project_name, 'techs': tech_stack}
        self.projects.append(project)
    def display_profile(self) -> None:
        print(f'=== Developer Hub: {self.developer_name} ===')
        print(f'Área: {self.major}')
        print(f'Projetos Ativos: {len(self.projects)}')
        for p in self.projects:
            print(f" - {p['name']} | Tecnologias: {', '.join(p['techs'])}")
if __name__ == '__main__':
    hub = PortfolioManager('Alyne', 'Sistemas de Informação')
    hub.add_project('3D Action Game (Godot)', ['GDScript', 'Game Dev'])
    hub.add_project('Developer Hub e Portfolio', ['Python', 'Git / GitHub'])
    hub.display_profile()