from pydantic import BaseModel 


class Fernando:
    name = "Fernando"
    idade = 39

    def __str__(self):
        return f"{self.name} - {self.idade} anos"
    

class TeacherFernando(Fernando):
    institution = "Infnet"

    def is_teacher(self):
        return "Professor at " +  self.institution


class User(BaseModel):
    id: int
    name: str
    email: str

    def __str__(self):
        return f"User({self.name} ({self.email}) )"

   
def example_user_pydantic():
    user_data = {
        "id": 1,
        "name": "Caboclo Pereira",
        "email": "caboclo.surfista@gmail.com"
    }
    user = User(id=user_data["id"],
                name=user_data["name"],
                email=user_data["email"])
    print(user)


def example_fernando():
    f = TeacherFernando()
    print(f)
    print(f.is_teacher())


if __name__ == "__main__":
    example_user_pydantic()