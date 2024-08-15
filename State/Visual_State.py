import reflex as rx
import requests as rq
from Magic_Tricks_d.components.components import seg_h,float_to_str
import csv
import io

back ="https://magic-back.onrender.com"

class VisualState(rx.State):
    loader: bool = False
    rough : list[list] #bruto
    dia: int = 0
    año : int = 0
    uni : str = ""
    error: bool = False
    success: bool = False

    @rx.background
    async def Visual_Service(self):
        async with self:
            self.loader = True
            self.error = False
            self.success = False
            try:
                response = rq.get(f"{back}/number/call_uad", params={"uni": self.uni, "año": self.año, "dia": self.dia})
                if response.status_code == 200:
                    rough_data = response.json()
                    self.rough = [[row[0],float_to_str(seg_h(row[1])),row[2],row[3]]for row in rough_data]
                    self.loader = False
                    self.success = True
                else:
                    self.loader = False
                    self.error = True
            except Exception as e:
                self.loader = False
                self.error = True
                print(f"Error: {e}")

    def _convert_to_csv(self) -> str:
        fieldnames = ["Ronda", "Hora", "Votos", "Propios"]
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(fieldnames)
        for row in self.rough:
            writer.writerow(row)
        csv_data = output.getvalue()
        output.close()
        return csv_data

    def download_csv_data(self):
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="data.csv",
        )
    
    def set_dia(self, value: int):
        self.dia = value


    def set_año(self, value: int):
        self.año = value

    def set_uni(self, value: str):
        self.uni = value

    @rx.var
    def uni_empty(self) -> bool:
        return not self.uni.strip()


    @rx.var
    def año_empty(self) -> bool:
        return self.año == 0

    @rx.var
    def dia_empty(self) -> bool:
        return self.dia == 0

    @rx.var
    def validate_fields_t(self) -> bool:
        return (self.uni_empty or self.año_empty or self.dia_empty)
    
    