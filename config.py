from pathlib import Path
from pydantic import BaseModel

class Profile(BaseModel):
    protocol: str
    host: str
    port: str
class Auth(BaseModel):
    username: str
    password: str
class GraphDB(BaseModel):
    profile: Profile
    auth: Auth

class Classifier(BaseModel):
    disease: str
    department: str
    check: str
    drug: str
    food: str
    producer: str
    symptom: str
    deny: str
class FPath(BaseModel):
    medical: str
    classifier: Classifier
    

class Config(BaseModel):
    graphDB: GraphDB
    path: FPath

def init_config() -> Config:
    path = Path('./config.json')
    c = Config.parse_file(path)
    return c

CONFIG = init_config()

def gen_graph_conn_params():
    params = ''
    if "py2neo":
        _p = CONFIG.graphDB.profile
        _a = CONFIG.graphDB.auth
        profile = f'{_p.protocol}://{_p.host}:{_p.port}'
        auth = (_a.username, _a.password)
        params = {"profile": profile, "auth": auth}
    return params


if __name__ == "__main__":
    print(CONFIG.dict())
