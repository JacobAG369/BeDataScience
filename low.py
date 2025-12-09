import os
from pathlib import Path

ROOT_DIR_NAME = "00_Roadmap"

def crear_readme_general(root_path: Path):
    contenido = """# 📘 BeDataScience – Roadmap a Data Scientist (24 Semanas)
Este directorio contiene todo el material, ejercicios, notas y proyectos
del plan profesional para convertirme en Data Scientist y AI Engineer.
"""
    readme_path = root_path / "README_GENERAL.md"
    readme_path.write_text(contenido, encoding="utf-8")

def crear_readme_dia(dia_path: Path, nombre_dia: str):
    contenido = f"""# {nombre_dia}

Este directorio contiene los ejercicios, notas y proyectos realizados durante {nombre_dia}.
"""
    (dia_path / "README.md").write_text(contenido, encoding="utf-8")

def main():
    root_path = Path.cwd() / ROOT_DIR_NAME
    root_path.mkdir(exist_ok=True)

    crear_readme_general(root_path)

    total_semanas = 24
    dias_por_semana = 7

    for semana in range(1, total_semanas + 1):
        semana_dir = root_path / f"Semana_{semana:02d}"
        semana_dir.mkdir(exist_ok=True)

        for dia_index in range(1, dias_por_semana + 1):
            dia_global = (semana - 1) * dias_por_semana + dia_index
            nombre_dia = f"Dia_{dia_global:02d}"
            dia_dir = semana_dir / nombre_dia
            dia_dir.mkdir(exist_ok=True)

            # Día 1 tiene estructura especial
            if dia_global == 1:
                (dia_dir / "ejercicios_python").mkdir(exist_ok=True)
                (dia_dir / "mini_proyecto").mkdir(exist_ok=True)
                (dia_dir / "notas").mkdir(exist_ok=True)
            else:
                (dia_dir / "ejercicios").mkdir(exist_ok=True)
                (dia_dir / "proyecto").mkdir(exist_ok=True)
                (dia_dir / "notas").mkdir(exist_ok=True)

            crear_readme_dia(dia_dir, f"Semana {semana:02d} – {nombre_dia}")

if __name__ == "__main__":
    main()
