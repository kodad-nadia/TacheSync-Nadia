import uuid
import unittest
from fastapi import APIRouter, HTTPException
from classes.schema_dto import Task, TaskNoID



class TestModels(unittest.TestCase):

    def test_task_model(self):
        # Créer une instance de modèle Task
        task = Task(id="1", name="Task Name", description="Task Description", completed=False)
        
        # Vérifier les attributs du modèle
        self.assertEqual(task.id, "1")
        self.assertEqual(task.name, "Task Name")
        self.assertEqual(task.description, "Task Description")
        self.assertFalse(task.completed)

    