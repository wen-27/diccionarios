import datamodels.modelsdata as models
def add_skill():
    skill = {
        "nombre":"",
        "proyectos": {
            "nota": 0.0
        },
        "examenes": {
            "nota": 0.0
        },
        "actividades": {
            "notas": {
                "quices": [],
                "retos": [],
                "tarea": []
            }
        }       
    }
    id = str(len(models.skills) + 1).zfill(4)  # Generate a new ID based on the current number of routes
    print(f'Id: {id}')
    skill['nombre'] = input("Ingrese el nombre de la skill: ")
    models.skills.update({id: skill})
    print(f'Skill {models.skills}')
    input("Presione Enter para continuar...")