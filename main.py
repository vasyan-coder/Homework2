import requests
import graphviz


def info(package_name, depth=0):
    global dot
    if depth >= 2:
        return

    try:
        r = requests.get(f"https://pypi.org/pypi/{package_name}/json").json()
        dependencies = r["info"]["requires_dist"]
        for i in range(len(dependencies)):
            dependencies[i] = dependencies[i].split()[0]
        dependencies = set(dependencies)
        for dep in dependencies:
            dot.edge(package_name, dep)
            info(dep, depth + 1)
    except:
        return


if __name__ == '__main__':
    package_name = input("Input package name: ").capitalize()
    dot = graphviz.Digraph()
    info(package_name)
    print(dot.source)
