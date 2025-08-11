from pydantic import BaseModel, Field
from typing import Optional

class Press20Row(BaseModel):
    shot_num: Optional[int]
    cameratimestamp: Optional[str]
    machinetimestamp: Optional[str]
    bottompassfail: Optional[str]
    toppassfail: Optional[str]
    overallpassfail: Optional[str]

    actcycletime: Optional[float]
    actclpclstime: Optional[float]
    actcoolingtime: Optional[float]

    actcushionposition: Optional[float]
    actinjectionpos: Optional[float]
    actinjfillspd: Optional[float]

    inj_act_prs_0: Optional[float]
    inj_act_prs_1: Optional[float]
    inj_act_prs_2: Optional[float]

    actnozzlecurrent: Optional[float]
    actcurrentservodrive_disp_1: Optional[float]
    actcurrentservodrive_disp_2: Optional[float]

    actnozzletemp: Optional[float]
    actzone1temp: Optional[float]
    actzone2temp: Optional[float]

    # Add more fields as needed following the data_descriptions.md

    class Config:
        extra = 'ignore'
