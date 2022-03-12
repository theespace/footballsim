import names
import random
import pandas as pd
see = pd.read_csv(r"https://docs.google.com/spreadsheets/d/e/2PACX-1vSm_AWiFbb16iKQxjSPS3XPcbYvs6A0AMiwEgkokU5KePTx1laaBsWiiNU9e9H77s0toTCgr-OxrELe/pub?output=csv")
see.to_csv("college_list",index=False)
college_list = pd.read_csv("college_list")
colleges = pd.DataFrame(data=college_list)

class Player:

    def set_up_player(self):
        global colleges
        positions = ["qb","lt","lg",
                     "c","rg","rt",
                     "le","re","edge",
                     "rolb","lolb",
                     "fs","ss"] * 2 + ["hb","te","mlb","dt"] * 3 + ["fb","p","k","ls"] + ["wr","cb"] * 6
        overalls = ["Elite"] * 3 + ["Superstar"] * 7 + ["Star"] * 10 + ["Normal"] * 80
        self.age = int(random.gauss(26,3))
        if self.age < 21:
            self.age = 21
        college_selector = random.randint(0,17132)
        self.college = colleges.at[college_selector,"Colleges"]
        self.status = "Active"
        self.exp = int(self.age - 21)
        self.contract_yrs_left = random.randint(1,7)
        self.first_name = names.get_first_name(gender='male')
        self.last_name = names.get_last_name()
        self.full_name = self.first_name + " " + self.last_name
        self.position = random.choice(positions)
        if self.position == "qb":
            self.height = random.randint(70,80)
            self.weight = random.randint(200,250)
        elif self.position == "hb":
            self.height = random.randint(66,77)
            self.weight = random.randint(180,230)
        elif self.position == "fb":
            self.height = random.randint(66,80)
            self.weight = random.randint(200,275)
        elif self.position == "te" or "ls":
            self.height = random.randint(70,80)
            self.weight = random.randint(200,275)
        elif self.position == "wr" or "cb" or "fs" or "ss" or "k" or "p":
            self.height = random.randint(68, 80)
            self.weight = random.randint(170, 230)
        elif self.position == "lt" or "lg" or "c" or "rg" or "rt" or "le" or "re" or "dt":
            self.height = random.randint(70, 80)
            self.weight = random.randint(230, 310)
        elif self.position == "egde" or "lolb" or "rolb" or "mlb":
            self.height = random.randint(70, 80)
            self.weight = random.randint(230, 310)
        self.ovr_rating = random.choice(overalls)
        if self.ovr_rating == "Elite":
            self.ovr_rating = random.randint(95,99)
        elif self.ovr_rating == "Superstar":
            self.ovr_rating = random.randint(85,95)
        elif self.ovr_rating == "Star":
            self.ovr_rating = random.randint(75,85)
        elif self.ovr_rating == "Normal":
            self.ovr_rating = random.randint(55,75)

    def age_up(self):
        self.age = int(self.age + 1)
        self.exp = int(self.exp + 1)
        if self.age > 30:
            self.ovr_rating = self.ovr_rating - random.randint(-1,5)
        else:
            self.ovr_rating = self.ovr_rating + random.randint(-1,5)

free_agents = []

def create_free_agents():
    global free_agents
    fa_player_count = len(free_agents)
    print("Creating Players...")
    while fa_player_count < 5000:
        new_player = Player()
        new_player.set_up_player()
        free_agents.append(new_player)
        current_player = free_agents[fa_player_count - 1]
        fa_player_count = len(free_agents)
    fa_names = [Player.full_name for Player in free_agents]
    fa_positions = [Player.position for Player in free_agents]
    fa_ovrs = [Player.ovr_rating for Player in free_agents]
    fa_colleges = [Player.college for Player in free_agents]
    fa_age = [Player.age for Player in free_agents]
    fa_exps = [Player.exp for Player in free_agents]
    fa_height = [Player.height for Player in free_agents]
    fa_weight = [Player.weight for Player in free_agents]
    fas = {"Name: ":fa_names,"Position: ":fa_positions,"Overall: ":fa_ovrs,"College: ":fa_colleges,"Age: ":fa_age,"Experience: ":fa_exps,"Height(inches): ":fa_height,"Weight(lbs): ":fa_weight}
    fa_df = pd.DataFrame(data=fas)
    fa_df.to_csv('freeagents.csv')
    fa_df = pd.read_csv('freeagents.csv')

rosters = []

class Roster:
    global free_agents
    global rosters
    def __init__(self,qbs,hbs,fbs,tes,wrs,lts,lgs,cs,rgs,rts,les,res,dts,edges,lolbs,rolbs,mlbs,cbs,fss,sss,ps,ks,lss,numbers_avail):
        self.qbs = []
        self.hbs = []
        self.fbs = []
        self.tes = []
        self.wrs = []
        self.lts = []
        self.lgs = []
        self.cs = []
        self.rgs = []
        self.rts = []
        self.les = []
        self.res = []
        self.dts = []
        self.edges = []
        self.lolbs = []
        self.rolbs = []
        self.mlbs = []
        self.cbs = []
        self.fss = []
        self.sss = []
        self.ps = []
        self.ks = []
        self.lss = []
        self.numbers_avail = list(range(1,100))

    def sign_qbs(self,Player):
        global free_agents
        fa_qbs = [Player for Player in free_agents if Player.position == "qb"]
        free_agents = [Player for Player in free_agents if Player not in fa_qbs]
        remaining_fa_qbs = fa_qbs
        qb_numbers = list(range(1,20))
        if len(self.qbs) == 0:
            new_qb1 = random.choice(fa_qbs)
            self.qbs.append(new_qb1)
            new_qb1.number = random.choice(qb_numbers)
            while new_qb1.number not in self.numbers_avail:
                new_qb1.number = random.choice(qb_numbers)
            qb_numbers.remove(int(new_qb1.number))
            self.numbers_avail.remove(int(new_qb1.number))
            print("QB " + new_qb1.full_name + ", #" + str(new_qb1.number) + " signed.")

        if len(self.qbs) == 1:
            new_qb2 = random.choice(fa_qbs)
            while new_qb2.full_name == new_qb1.full_name:
                new_qb2 = random.choice(fa_qbs)
            self.qbs.append(new_qb2)
            new_qb2.number = random.choice(qb_numbers)
            while new_qb2.number not in self.numbers_avail:
                new_qb2.number = random.choice(qb_numbers)
            qb_numbers.remove(int(new_qb2.number))
            self.numbers_avail.remove(int(new_qb2.number))
            print("QB " + new_qb2.full_name + ", #" + str(new_qb2.number) + " signed.")
            remaining_fa_qbs = [Player for Player in fa_qbs if Player.full_name != new_qb1.full_name
                            or Player.full_name != new_qb2.full_name]
        free_agents.extend(remaining_fa_qbs)

    def sign_hbs(self,Player):
        global free_agents
        fa_hbs = [Player for Player in free_agents if Player.position == "hb"]
        free_agents = [Player for Player in free_agents if Player not in fa_hbs]
        remaining_fa_hbs = fa_hbs
        hb_numbers = list(range(1,50))
        if len(self.hbs) == 0:
            new_hb1 = random.choice(fa_hbs)
            self.hbs.append(new_hb1)
            new_hb1.number = random.choice(hb_numbers)
            while new_hb1.number not in self.numbers_avail:
                new_hb1.number = random.choice(hb_numbers)
            hb_numbers.remove(int(new_hb1.number))
            self.numbers_avail.remove(int(new_hb1.number))
            print("HB " + new_hb1.full_name + ", #" + str(new_hb1.number) + " signed.")

        if len(self.hbs) == 1:
            new_hb2 = random.choice(fa_hbs)
            while new_hb2.full_name == new_hb1.full_name:
                new_hb2 = random.choice(fa_hbs)
            self.hbs.append(new_hb2)
            new_hb2.number = random.choice(hb_numbers)
            while new_hb2.number not in self.numbers_avail:
                new_hb2.number = random.choice(hb_numbers)
            hb_numbers.remove(int(new_hb2.number))
            self.numbers_avail.remove(int(new_hb2.number))
            print("HB " + new_hb2.full_name + ", #" + str(new_hb2.number) + " signed.")
           
        if len(self.hbs) == 2:
            new_hb3 = random.choice(fa_hbs)
            while new_hb3.full_name == new_hb1.full_name or new_hb3.full_name == new_hb2.full_name:
                new_hb3 = random.choice(fa_hbs)
            self.hbs.append(new_hb3)
            new_hb3.number = random.choice(hb_numbers)
            while new_hb3.number not in self.numbers_avail:
                new_hb3.number = random.choice(hb_numbers)
            hb_numbers.remove(int(new_hb3.number))
            self.numbers_avail.remove(int(new_hb3.number))
            print("HB " + new_hb3.full_name + ", #" + str(new_hb3.number) + " signed.")
            remaining_fa_hbs = [Player for Player in fa_hbs if Player.full_name != new_hb1.full_name
                            or Player.full_name != new_hb2.full_name
                            or Player.full_name != new_hb3.full_name]
        free_agents.extend(remaining_fa_hbs)

    def sign_fbs(self,Player):
        global free_agents
        fa_fbs = [Player for Player in free_agents if Player.position == "fb"]
        free_agents = [Player for Player in free_agents if Player not in fa_fbs]
        remaining_fa_fbs = fa_fbs
        fb_numbers = list(range(1,50))
        if len(self.fbs) == 0:
            new_fb1 = random.choice(fa_fbs)
            self.fbs.append(new_fb1)
            new_fb1.number = random.choice(fb_numbers)
            while new_fb1.number not in self.numbers_avail:
                new_fb1.number = random.choice(fb_numbers)
            fb_numbers.remove(int(new_fb1.number))
            self.numbers_avail.remove(int(new_fb1.number))
            print("FB " + new_fb1.full_name + ", #" + str(new_fb1.number) + " signed.")
            remaining_fa_fbs = [Player for Player in fa_fbs if Player.full_name is not new_fb1.full_name]
        free_agents.extend(remaining_fa_fbs)

    def sign_tes(self,Player):
        global free_agents
        fa_tes = [Player for Player in free_agents if Player.position == "te"]
        free_agents = [Player for Player in free_agents if Player not in fa_tes]
        remaining_fa_tes = fa_tes
        te_numbers = list(range(1,50)) + list(range(80,90))
        if len(self.tes) == 0:
            new_te1 = random.choice(fa_tes)
            self.tes.append(new_te1)
            new_te1.number = random.choice(te_numbers)
            while new_te1.number not in self.numbers_avail:
                new_te1.number = random.choice(te_numbers)
            te_numbers.remove(int(new_te1.number))
            self.numbers_avail.remove(int(new_te1.number))
            print("TE " + new_te1.full_name + ", #" + str(new_te1.number) + " signed.")

        if len(self.tes) == 1:
            new_te2 = random.choice(fa_tes)
            while new_te2.full_name == new_te1.full_name:
                new_te2 = random.choice(fa_tes)
            self.tes.append(new_te2)
            new_te2.number = random.choice(te_numbers)
            while new_te2.number not in self.numbers_avail:
                new_te2.number = random.choice(te_numbers)
            te_numbers.remove(int(new_te2.number))
            self.numbers_avail.remove(int(new_te2.number))
            print("TE " + new_te2.full_name + ", #" + str(new_te2.number) + " signed.")

        if len(self.tes) == 2:
            new_te3 = random.choice(fa_tes)
            while new_te3.full_name == new_te1.full_name or new_te3.full_name == new_te2.full_name:
                new_te3 = random.choice(fa_tes)
            self.tes.append(new_te3)
            new_te3.number = random.choice(te_numbers)
            while new_te3.number not in self.numbers_avail:
                new_te3.number = random.choice(te_numbers)
            te_numbers.remove(int(new_te3.number))
            self.numbers_avail.remove(int(new_te3.number))
            print("TE " + new_te3.full_name + ", #" + str(new_te3.number) + " signed.")
            remaining_fa_tes = [Player for Player in fa_tes if Player.full_name != new_te1.full_name
                            or Player.full_name != new_te2.full_name
                            or Player.full_name != new_te3.full_name]
        free_agents.extend(remaining_fa_tes)
            
    def sign_wrs(self,Player):
        global free_agents
        fa_wrs = [Player for Player in free_agents if Player.position == "wr"]
        free_agents = [Player for Player in free_agents if Player not in fa_wrs]
        remaining_fa_wrs = fa_wrs
        wr_numbers = list(range(1,20)) + list(range(80,90))
        if len(self.wrs) == 0:
            new_wr1 = random.choice(fa_wrs)
            self.wrs.append(new_wr1)
            new_wr1.number = random.choice(wr_numbers)
            while new_wr1.number not in self.numbers_avail:
                new_wr1.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr1.number))
            self.numbers_avail.remove(int(new_wr1.number))
            print("WR " + new_wr1.full_name + ", #" + str(new_wr1.number) + " signed.")

        if len(self.wrs) == 1:
            new_wr2 = random.choice(fa_wrs)
            while new_wr2.full_name == new_wr1.full_name:
                new_wr2 = random.choice(fa_wrs)
            self.wrs.append(new_wr2)
            new_wr2.number = random.choice(wr_numbers)
            while new_wr2.number not in self.numbers_avail:
                new_wr2.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr2.number))
            self.numbers_avail.remove(int(new_wr2.number))
            print("WR " + new_wr2.full_name + ", #" + str(new_wr2.number) + " signed.")

        if len(self.wrs) == 2:
            new_wr3 = random.choice(fa_wrs)
            while new_wr3.full_name == new_wr1.full_name or new_wr3.full_name == new_wr2.full_name:
                new_wr3 = random.choice(fa_wrs)
            self.wrs.append(new_wr3)
            new_wr3.number = random.choice(wr_numbers)
            while new_wr3.number not in self.numbers_avail:
                new_wr3.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr3.number))
            self.numbers_avail.remove(int(new_wr3.number))
            print("WR " + new_wr3.full_name + ", #" + str(new_wr3.number) + " signed.")

        if len(self.wrs) == 3:
            new_wr4 = random.choice(fa_wrs)
            while new_wr4.full_name == new_wr1.full_name \
                    or new_wr4.full_name == new_wr2.full_name \
                    or new_wr4.full_name == new_wr3.full_name:
                new_wr4 = random.choice(fa_wrs)
            self.wrs.append(new_wr4)
            new_wr4.number = random.choice(wr_numbers)
            while new_wr4.number not in self.numbers_avail:
                new_wr4.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr4.number))
            self.numbers_avail.remove(int(new_wr4.number))
            print("WR " + new_wr4.full_name + ", #" + str(new_wr4.number) + " signed.")

        if len(self.wrs) == 4:
            new_wr5 = random.choice(fa_wrs)
            while new_wr5.full_name == new_wr1.full_name \
                    or new_wr5.full_name == new_wr2.full_name \
                    or new_wr5.full_name == new_wr3.full_name \
                    or new_wr5.full_name == new_wr4.full_name:
                new_wr5 = random.choice(fa_wrs)
            self.wrs.append(new_wr5)
            new_wr5.number = random.choice(wr_numbers)
            while new_wr5.number not in self.numbers_avail:
                new_wr5.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr5.number))
            self.numbers_avail.remove(int(new_wr5.number))
            print("WR " + new_wr5.full_name + ", #" + str(new_wr5.number) + " signed.")
        
        if len(self.wrs) == 5:
            new_wr6 = random.choice(fa_wrs)
            while new_wr6.full_name == new_wr1.full_name \
                    or new_wr6.full_name == new_wr2.full_name \
                    or new_wr6.full_name == new_wr3.full_name \
                    or new_wr6.full_name == new_wr4.full_name \
                    or new_wr6.full_name == new_wr5.full_name:
                new_wr6 = random.choice(fa_wrs)
            self.wrs.append(new_wr6)
            new_wr6.number = random.choice(wr_numbers)
            while new_wr6.number not in self.numbers_avail:
                new_wr6.number = random.choice(wr_numbers)
            wr_numbers.remove(int(new_wr6.number))
            self.numbers_avail.remove(int(new_wr6.number))
            print("WR " + new_wr6.full_name + ", #" + str(new_wr6.number) + " signed.")
            remaining_fa_wrs = [Player for Player in fa_wrs if Player.full_name != new_wr1.full_name
                            or Player.full_name != new_wr2.full_name
                            or Player.full_name != new_wr3.full_name
                            or Player.full_name != new_wr4.full_name
                            or Player.full_name != new_wr5.full_name
                            or Player.full_name != new_wr6.full_name]
        free_agents.extend(remaining_fa_wrs)
        
    def sign_lts(self,Player):
        global free_agents
        fa_lts = [Player for Player in free_agents if Player.position == "lt"]
        free_agents = [Player for Player in free_agents if Player not in fa_lts]
        remaining_fa_lts = fa_lts
        lt_numbers = list(range(50,80))
        if len(self.lts) == 0:
            new_lt1 = random.choice(fa_lts)
            self.lts.append(new_lt1)
            new_lt1.number = random.choice(lt_numbers)
            while new_lt1.number not in self.numbers_avail:
                new_lt1.number = random.choice(lt_numbers)
            lt_numbers.remove(int(new_lt1.number))
            self.numbers_avail.remove(int(new_lt1.number))
            print("LT " + new_lt1.full_name + ", #" + str(new_lt1.number) + " signed.")

        if len(self.lts) == 1:
            new_lt2 = random.choice(fa_lts)
            while new_lt2.full_name == new_lt1.full_name:
                new_lt2 = random.choice(fa_lts)
            self.lts.append(new_lt2)
            new_lt2.number = random.choice(lt_numbers)
            while new_lt2.number not in self.numbers_avail:
                new_lt2.number = random.choice(lt_numbers)
            lt_numbers.remove(int(new_lt2.number))
            self.numbers_avail.remove(int(new_lt2.number))
            print("LT " + new_lt2.full_name + ", #" + str(new_lt2.number) + " signed.")
            remaining_fa_lts = [Player for Player in fa_lts if Player.full_name != new_lt1.full_name
                            or Player.full_name != new_lt2.full_name]
        free_agents.extend(remaining_fa_lts)

    def sign_lgs(self,Player):
        global free_agents
        fa_lgs = [Player for Player in free_agents if Player.position == "lg"]
        free_agents = [Player for Player in free_agents if Player not in fa_lgs]
        remaining_fa_lgs = fa_lgs
        lg_numbers = list(range(50,80))
        if len(self.lgs) == 0:
            new_lg1 = random.choice(fa_lgs)
            self.lgs.append(new_lg1)
            new_lg1.number = random.choice(lg_numbers)
            while new_lg1.number not in self.numbers_avail:
                new_lg1.number = random.choice(lg_numbers)
            lg_numbers.remove(int(new_lg1.number))
            self.numbers_avail.remove(int(new_lg1.number))
            print("LG " + new_lg1.full_name + ", #" + str(new_lg1.number) + " signed.")

        if len(self.lgs) == 1:
            new_lg2 = random.choice(fa_lgs)
            while new_lg2.full_name == new_lg1.full_name:
                new_lg2 = random.choice(fa_lgs)
            self.lgs.append(new_lg2)
            new_lg2.number = random.choice(lg_numbers)
            while new_lg2.number not in self.numbers_avail:
                new_lg2.number = random.choice(lg_numbers)
            lg_numbers.remove(int(new_lg2.number))
            self.numbers_avail.remove(int(new_lg2.number))
            print("LG " + new_lg2.full_name + ", #" + str(new_lg2.number) + " signed.")
            remaining_fa_lgs = [Player for Player in fa_lgs if Player.full_name != new_lg1.full_name
                            or Player.full_name != new_lg2.full_name]
        free_agents.extend(remaining_fa_lgs)

    def sign_cs(self,Player):
        global free_agents
        fa_cs = [Player for Player in free_agents if Player.position == "c"]
        free_agents = [Player for Player in free_agents if Player not in fa_cs]
        remaining_fa_cs = fa_cs
        c_numbers = list(range(50,80))
        if len(self.cs) == 0:
            new_c1 = random.choice(fa_cs)
            self.cs.append(new_c1)
            new_c1.number = random.choice(c_numbers)
            while new_c1.number not in self.numbers_avail:
                new_c1.number = random.choice(c_numbers)
            c_numbers.remove(int(new_c1.number))
            self.numbers_avail.remove(int(new_c1.number))
            print("C " + new_c1.full_name + ", #" + str(new_c1.number) + " signed.")

        if len(self.cs) == 1:
            new_c2 = random.choice(fa_cs)
            while new_c2.full_name == new_c1.full_name:
                new_c2 = random.choice(fa_cs)
            self.cs.append(new_c2)
            new_c2.number = random.choice(c_numbers)
            while new_c2.number not in self.numbers_avail:
                new_c2.number = random.choice(c_numbers)
            c_numbers.remove(int(new_c2.number))
            self.numbers_avail.remove(int(new_c2.number))
            print("C " + new_c2.full_name + ", #" + str(new_c2.number) + " signed.")
            remaining_fa_cs = [Player for Player in fa_cs if Player.full_name != new_c1.full_name
                            or Player.full_name != new_c2.full_name]
        free_agents.extend(remaining_fa_cs)
            
    def sign_rgs(self,Player):
        global free_agents
        fa_rgs = [Player for Player in free_agents if Player.position == "rg"]
        free_agents = [Player for Player in free_agents if Player not in fa_rgs]
        remaining_fa_rgs = fa_rgs
        rg_numbers = list(range(50,80))
        if len(self.rgs) == 0:
            new_rg1 = random.choice(fa_rgs)
            self.rgs.append(new_rg1)
            new_rg1.number = random.choice(rg_numbers)
            while new_rg1.number not in self.numbers_avail:
                new_rg1.number = random.choice(rg_numbers)
            rg_numbers.remove(int(new_rg1.number))
            self.numbers_avail.remove(int(new_rg1.number))
            print("RG " + new_rg1.full_name + ", #" + str(new_rg1.number) + " signed.")

        if len(self.rgs) == 1:
            new_rg2 = random.choice(fa_rgs)
            while new_rg2.full_name == new_rg1.full_name:
                new_rg2 = random.choice(fa_rgs)
            self.rgs.append(new_rg2)
            new_rg2.number = random.choice(rg_numbers)
            while new_rg2.number not in self.numbers_avail:
                new_rg2.number = random.choice(rg_numbers)
            rg_numbers.remove(int(new_rg2.number))
            self.numbers_avail.remove(int(new_rg2.number))
            print("RG " + new_rg2.full_name + ", #" + str(new_rg2.number) + " signed.")
            remaining_fa_rgs = [Player for Player in fa_rgs if Player.full_name != new_rg1.full_name
                            or Player.full_name != new_rg2.full_name]
        free_agents.extend(remaining_fa_rgs)

    def sign_rts(self,Player):
        global free_agents
        fa_rts = [Player for Player in free_agents if Player.position == "rt"]
        free_agents = [Player for Player in free_agents if Player not in fa_rts]
        remaining_fa_rts = fa_rts
        rt_numbers = list(range(50,80))
        if len(self.rts) == 0:
            new_rt1 = random.choice(fa_rts)
            self.rts.append(new_rt1)
            new_rt1.number = random.choice(rt_numbers)
            while new_rt1.number not in self.numbers_avail:
                new_rt1.number = random.choice(rt_numbers)
            rt_numbers.remove(int(new_rt1.number))
            self.numbers_avail.remove(int(new_rt1.number))
            print("RT " + new_rt1.full_name + ", #" + str(new_rt1.number) + " signed.")

        if len(self.rts) == 1:
            new_rt2 = random.choice(fa_rts)
            while new_rt2.full_name == new_rt1.full_name:
                new_rt2 = random.choice(fa_rts)
            self.rts.append(new_rt2)
            new_rt2.number = random.choice(rt_numbers)
            while new_rt2.number not in self.numbers_avail:
                new_rt2.number = random.choice(rt_numbers)
            rt_numbers.remove(int(new_rt2.number))
            self.numbers_avail.remove(int(new_rt2.number))
            print("RT " + new_rt2.full_name + ", #" + str(new_rt2.number) + " signed.")
            remaining_fa_rts = [Player for Player in fa_rts if Player.full_name != new_rt1.full_name
                            or Player.full_name != new_rt2.full_name]
        free_agents.extend(remaining_fa_rts)
            
    def sign_les(self,Player):
        global free_agents
        fa_les = [Player for Player in free_agents if Player.position == "le"]
        free_agents = [Player for Player in free_agents if Player not in fa_les]
        remaining_fa_les = fa_les
        le_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.les) == 0:
            new_le1 = random.choice(fa_les)
            self.les.append(new_le1)
            new_le1.number = random.choice(le_numbers)
            while new_le1.number not in self.numbers_avail:
                new_le1.number = random.choice(le_numbers)
            le_numbers.remove(int(new_le1.number))
            self.numbers_avail.remove(int(new_le1.number))
            print("LE " + new_le1.full_name + ", #" + str(new_le1.number) + " signed.")

        if len(self.les) == 1:
            new_le2 = random.choice(fa_les)
            while new_le2.full_name == new_le1.full_name:
                new_le2 = random.choice(fa_les)
            self.les.append(new_le2)
            new_le2.number = random.choice(le_numbers)
            while new_le2.number not in self.numbers_avail:
                new_le2.number = random.choice(le_numbers)
            le_numbers.remove(int(new_le2.number))
            self.numbers_avail.remove(int(new_le2.number))
            print("LE " + new_le2.full_name + ", #" + str(new_le2.number) + " signed.")
            remaining_fa_les = [Player for Player in fa_les if Player.full_name != new_le1.full_name
                            or Player.full_name != new_le2.full_name]
        free_agents.extend(remaining_fa_les)
            
    def sign_res(self,Player):
        global free_agents
        fa_res = [Player for Player in free_agents if Player.position == "re"]
        free_agents = [Player for Player in free_agents if Player not in fa_res]
        remaining_fa_res = fa_res
        re_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.res) == 0:
            new_re1 = random.choice(fa_res)
            self.res.append(new_re1)
            new_re1.number = random.choice(re_numbers)
            while new_re1.number not in self.numbers_avail:
                new_re1.number = random.choice(re_numbers)
            re_numbers.remove(int(new_re1.number))
            self.numbers_avail.remove(int(new_re1.number))
            print("RE " + new_re1.full_name + ", #" + str(new_re1.number) + " signed.")

        if len(self.res) == 1:
            new_re2 = random.choice(fa_res)
            while new_re2.full_name == new_re1.full_name:
                new_re2 = random.choice(fa_res)
            self.res.append(new_re2)
            new_re2.number = random.choice(re_numbers)
            while new_re2.number not in self.numbers_avail:
                new_re2.number = random.choice(re_numbers)
            re_numbers.remove(int(new_re2.number))
            self.numbers_avail.remove(int(new_re2.number))
            print("RE " + new_re2.full_name + ", #" + str(new_re2.number) + " signed.")
            remaining_fa_res = [Player for Player in fa_res if Player.full_name != new_re1.full_name
                            or Player.full_name != new_re2.full_name]
        free_agents.extend(remaining_fa_res)
            
    def sign_dts(self,Player):
        global free_agents
        fa_dts = [Player for Player in free_agents if Player.position == "dt"]
        free_agents = [Player for Player in free_agents if Player not in fa_dts]
        remaining_fa_dts = fa_dts
        dt_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.dts) == 0:
            new_dt1 = random.choice(fa_dts)
            self.dts.append(new_dt1)
            new_dt1.number = random.choice(dt_numbers)
            while new_dt1.number not in self.numbers_avail:
                new_dt1.number = random.choice(dt_numbers)
            dt_numbers.remove(int(new_dt1.number))
            self.numbers_avail.remove(int(new_dt1.number))
            print("DT " + new_dt1.full_name + ", #" + str(new_dt1.number) + " signed.")

        if len(self.dts) == 1:
            new_dt2 = random.choice(fa_dts)
            while new_dt2.full_name == new_dt1.full_name:
                new_dt2 = random.choice(fa_dts)
            self.dts.append(new_dt2)
            new_dt2.number = random.choice(dt_numbers)
            while new_dt2.number not in self.numbers_avail:
                new_dt2.number = random.choice(dt_numbers)
            dt_numbers.remove(int(new_dt2.number))
            self.numbers_avail.remove(int(new_dt2.number))
            print("DT " + new_dt2.full_name + ", #" + str(new_dt2.number) + " signed.")

        if len(self.dts) == 2:
            new_dt3 = random.choice(fa_dts)
            while new_dt3.full_name == new_dt1.full_name or new_dt3.full_name == new_dt2.full_name:
                new_dt3 = random.choice(fa_dts)
            self.dts.append(new_dt3)
            new_dt3.number = random.choice(dt_numbers)
            while new_dt3.number not in self.numbers_avail:
                new_dt3.number = random.choice(dt_numbers)
            dt_numbers.remove(int(new_dt3.number))
            self.numbers_avail.remove(int(new_dt3.number))
            print("DT " + new_dt3.full_name + ", #" + str(new_dt3.number) + " signed.")
            remaining_fa_dts = [Player for Player in fa_dts if Player.full_name != new_dt1.full_name
                                or Player.full_name != new_dt2.full_name
                                or Player.full_name != new_dt3.full_name]
        free_agents.extend(remaining_fa_dts)
            
    def sign_edges(self,Player):
        global free_agents
        fa_edges = [Player for Player in free_agents if Player.position == "edge"]
        free_agents = [Player for Player in free_agents if Player not in fa_edges]
        remaining_fa_edges = fa_edges
        edge_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.edges) == 0:
            new_edge1 = random.choice(fa_edges)
            self.edges.append(new_edge1)
            new_edge1.number = random.choice(edge_numbers)
            while new_edge1.number not in self.numbers_avail:
                new_edge1.number = random.choice(edge_numbers)
            edge_numbers.remove(int(new_edge1.number))
            self.numbers_avail.remove(int(new_edge1.number))
            print("EDGE " + new_edge1.full_name + ", #" + str(new_edge1.number) + " signed.")

        if len(self.edges) == 1:
            new_edge2 = random.choice(fa_edges)
            while new_edge2.full_name == new_edge1.full_name:
                new_edge2 = random.choice(fa_edges)
            self.edges.append(new_edge2)
            new_edge2.number = random.choice(edge_numbers)
            while new_edge2.number not in self.numbers_avail:
                new_edge2.number = random.choice(edge_numbers)
            edge_numbers.remove(int(new_edge2.number))
            self.numbers_avail.remove(int(new_edge2.number))
            print("EDGE " + new_edge2.full_name + ", #" + str(new_edge2.number) + " signed.")
            remaining_fa_edges = [Player for Player in fa_edges if Player.full_name != new_edge1.full_name
                            or Player.full_name != new_edge2.full_name]
        free_agents.extend(remaining_fa_edges)
            
    def sign_lolbs(self,Player):
        global free_agents
        fa_lolbs = [Player for Player in free_agents if Player.position == "lolb"]
        free_agents = [Player for Player in free_agents if Player not in fa_lolbs]
        remaining_fa_lolbs = fa_lolbs
        lolb_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.lolbs) == 0:
            new_lolb1 = random.choice(fa_lolbs)
            self.lolbs.append(new_lolb1)
            new_lolb1.number = random.choice(lolb_numbers)
            while new_lolb1.number not in self.numbers_avail:
                new_lolb1.number = random.choice(lolb_numbers)
            lolb_numbers.remove(int(new_lolb1.number))
            self.numbers_avail.remove(int(new_lolb1.number))
            print("LOLB " + new_lolb1.full_name + ", #" + str(new_lolb1.number) + " signed.")

        if len(self.lolbs) == 1:
            new_lolb2 = random.choice(fa_lolbs)
            while new_lolb2.full_name == new_lolb1.full_name:
                new_lolb2 = random.choice(fa_lolbs)
            self.lolbs.append(new_lolb2)
            new_lolb2.number = random.choice(lolb_numbers)
            while new_lolb2.number not in self.numbers_avail:
                new_lolb2.number = random.choice(lolb_numbers)
            lolb_numbers.remove(int(new_lolb2.number))
            self.numbers_avail.remove(int(new_lolb2.number))
            print("LOLB " + new_lolb2.full_name + ", #" + str(new_lolb2.number) + " signed.")
            remaining_fa_lolbs = [Player for Player in fa_lolbs if Player.full_name != new_lolb1.full_name
                            or Player.full_name != new_lolb2.full_name]
        free_agents.extend(remaining_fa_lolbs)

    def sign_rolbs(self,Player):
        global free_agents
        fa_rolbs = [Player for Player in free_agents if Player.position == "rolb"]
        free_agents = [Player for Player in free_agents if Player not in fa_rolbs]
        remaining_fa_rolbs = fa_rolbs
        rolb_numbers = list(range(1,60)) + list(range(70,80))  + list(range(90,100))
        if len(self.rolbs) == 0:
            new_rolb1 = random.choice(fa_rolbs)
            self.rolbs.append(new_rolb1)
            new_rolb1.number = random.choice(rolb_numbers)
            while new_rolb1.number not in self.numbers_avail:
                new_rolb1.number = random.choice(rolb_numbers)
            rolb_numbers.remove(int(new_rolb1.number))
            self.numbers_avail.remove(int(new_rolb1.number))
            print("ROLB " + new_rolb1.full_name + ", #" + str(new_rolb1.number) + " signed.")

        if len(self.rolbs) == 1:
            new_rolb2 = random.choice(fa_rolbs)
            while new_rolb2.full_name == new_rolb1.full_name:
                new_rolb2 = random.choice(fa_rolbs)
            self.rolbs.append(new_rolb2)
            new_rolb2.number = random.choice(rolb_numbers)
            while new_rolb2.number not in self.numbers_avail:
                new_rolb2.number = random.choice(rolb_numbers)
            rolb_numbers.remove(int(new_rolb2.number))
            self.numbers_avail.remove(int(new_rolb2.number))
            print("ROLB " + new_rolb2.full_name + ", #" + str(new_rolb2.number) + " signed.")
            remaining_fa_rolbs = [Player for Player in fa_rolbs if Player.full_name != new_rolb1.full_name
                            or Player.full_name != new_rolb2.full_name]
        free_agents.extend(remaining_fa_rolbs)
            
    def sign_mlbs(self,Player):
        global free_agents
        fa_mlbs = [Player for Player in free_agents if Player.position == "mlb"]
        free_agents = [Player for Player in free_agents if Player not in fa_mlbs]
        remaining_fa_mlbs = fa_mlbs
        mlb_numbers = list(range(1,60)) + list(range(90,100))
        if len(self.mlbs) == 0:
            new_mlb1 = random.choice(fa_mlbs)
            self.mlbs.append(new_mlb1)
            new_mlb1.number = random.choice(mlb_numbers)
            while new_mlb1.number not in self.numbers_avail:
                new_mlb1.number = random.choice(mlb_numbers)
            mlb_numbers.remove(int(new_mlb1.number))
            self.numbers_avail.remove(int(new_mlb1.number))
            print("MLB " + new_mlb1.full_name + ", #" + str(new_mlb1.number) + " signed.")

        if len(self.mlbs) == 1:
            new_mlb2 = random.choice(fa_mlbs)
            while new_mlb2.full_name == new_mlb1.full_name:
                new_mlb2 = random.choice(fa_mlbs)
            self.mlbs.append(new_mlb2)
            new_mlb2.number = random.choice(mlb_numbers)
            while new_mlb2.number not in self.numbers_avail:
                new_mlb2.number = random.choice(mlb_numbers)
            mlb_numbers.remove(int(new_mlb2.number))
            self.numbers_avail.remove(int(new_mlb2.number))
            print("MLB " + new_mlb2.full_name + ", #" + str(new_mlb2.number) + " signed.")

        if len(self.mlbs) == 2:
            new_mlb3 = random.choice(fa_mlbs)
            while new_mlb3.full_name == new_mlb1.full_name or new_mlb3.full_name == new_mlb2.full_name:
                new_mlb3 = random.choice(fa_mlbs)
            self.mlbs.append(new_mlb3)
            new_mlb3.number = random.choice(mlb_numbers)
            while new_mlb3.number not in self.numbers_avail:
                new_mlb3.number = random.choice(mlb_numbers)
            mlb_numbers.remove(int(new_mlb3.number))
            self.numbers_avail.remove(int(new_mlb3.number))
            print("MLB " + new_mlb3.full_name + ", #" + str(new_mlb3.number) + " signed.")
            remaining_fa_mlbs = [Player for Player in fa_mlbs if Player.full_name != new_mlb1.full_name
                                or Player.full_name != new_mlb2.full_name
                                or Player.full_name != new_mlb3.full_name]
        free_agents.extend(remaining_fa_mlbs)
            
    def sign_cbs(self,Player):
        global free_agents
        fa_cbs = [Player for Player in free_agents if Player.position == "cb"]
        free_agents = [Player for Player in free_agents if Player not in fa_cbs]
        remaining_fa_cbs = fa_cbs
        cb_numbers = list(range(1, 50))
        if len(self.cbs) == 0:
            new_cb1 = random.choice(fa_cbs)
            self.cbs.append(new_cb1)
            new_cb1.number = random.choice(cb_numbers)
            while new_cb1.number not in self.numbers_avail:
                new_cb1.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb1.number))
            self.numbers_avail.remove(int(new_cb1.number))
            print("CB " + new_cb1.full_name + ", #" + str(new_cb1.number) + " signed.")

        if len(self.cbs) == 1:
            new_cb2 = random.choice(fa_cbs)
            while new_cb2.full_name == new_cb1.full_name:
                new_cb2 = random.choice(fa_cbs)
            self.cbs.append(new_cb2)
            new_cb2.number = random.choice(cb_numbers)
            while new_cb2.number not in self.numbers_avail:
                new_cb2.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb2.number))
            self.numbers_avail.remove(int(new_cb2.number))
            print("CB " + new_cb2.full_name + ", #" + str(new_cb2.number) + " signed.")

        if len(self.cbs) == 2:
            new_cb3 = random.choice(fa_cbs)
            while new_cb3.full_name == new_cb1.full_name or new_cb3.full_name == new_cb2.full_name:
                new_cb3 = random.choice(fa_cbs)
            self.cbs.append(new_cb3)
            new_cb3.number = random.choice(cb_numbers)
            while new_cb3.number not in self.numbers_avail:
                new_cb3.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb3.number))
            self.numbers_avail.remove(int(new_cb3.number))
            print("CB " + new_cb3.full_name + ", #" + str(new_cb3.number) + " signed.")

        if len(self.cbs) == 3:
            new_cb4 = random.choice(fa_cbs)
            while new_cb4.full_name == new_cb1.full_name \
                    or new_cb4.full_name == new_cb2.full_name \
                    or new_cb4.full_name == new_cb3.full_name:
                new_cb4 = random.choice(fa_cbs)
            self.cbs.append(new_cb4)
            new_cb4.number = random.choice(cb_numbers)
            while new_cb4.number not in self.numbers_avail:
                new_cb4.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb4.number))
            self.numbers_avail.remove(int(new_cb4.number))
            print("CB " + new_cb4.full_name + ", #" + str(new_cb4.number) + " signed.")

        if len(self.cbs) == 4:
            new_cb5 = random.choice(fa_cbs)
            while new_cb5.full_name == new_cb1.full_name \
                    or new_cb5.full_name == new_cb2.full_name \
                    or new_cb5.full_name == new_cb3.full_name \
                    or new_cb5.full_name == new_cb4.full_name:
                new_cb5 = random.choice(fa_cbs)
            self.cbs.append(new_cb5)
            new_cb5.number = random.choice(cb_numbers)
            while new_cb5.number not in self.numbers_avail:
                new_cb5.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb5.number))
            self.numbers_avail.remove(int(new_cb5.number))
            print("CB " + new_cb5.full_name + ", #" + str(new_cb5.number) + " signed.")

        if len(self.cbs) == 5:
            new_cb6 = random.choice(fa_cbs)
            while new_cb6.full_name == new_cb1.full_name \
                    or new_cb6.full_name == new_cb2.full_name \
                    or new_cb6.full_name == new_cb3.full_name \
                    or new_cb6.full_name == new_cb4.full_name \
                    or new_cb6.full_name == new_cb5.full_name:
                new_cb6 = random.choice(fa_cbs)
            self.cbs.append(new_cb6)
            new_cb6.number = random.choice(cb_numbers)
            while new_cb6.number not in self.numbers_avail:
                new_cb6.number = random.choice(cb_numbers)
            cb_numbers.remove(int(new_cb6.number))
            self.numbers_avail.remove(int(new_cb6.number))
            print("CB " + new_cb6.full_name + ", #" + str(new_cb6.number) + " signed.")
            remaining_fa_cbs = [Player for Player in fa_cbs if Player.full_name != new_cb1.full_name
                                or Player.full_name != new_cb2.full_name
                                or Player.full_name != new_cb3.full_name
                                or Player.full_name != new_cb4.full_name
                                or Player.full_name != new_cb5.full_name
                                or Player.full_name != new_cb6.full_name]
        free_agents.extend(remaining_fa_cbs)
            
    def sign_fss(self,Player):
        global free_agents
        fa_fss = [Player for Player in free_agents if Player.position == "fs"]
        free_agents = [Player for Player in free_agents if Player not in fa_fss]
        remaining_fa_fss = fa_fss
        fs_numbers = list(range(1,50))
        if len(self.fss) == 0:
            new_fs1 = random.choice(fa_fss)
            self.fss.append(new_fs1)
            new_fs1.number = random.choice(fs_numbers)
            while new_fs1.number not in self.numbers_avail:
                new_fs1.number = random.choice(fs_numbers)
            fs_numbers.remove(int(new_fs1.number))
            self.numbers_avail.remove(int(new_fs1.number))
            print("FS " + new_fs1.full_name + ", #" + str(new_fs1.number) + " signed.")

        if len(self.fss) == 1:
            new_fs2 = random.choice(fa_fss)
            while new_fs2.full_name == new_fs1.full_name:
                new_fs2 = random.choice(fa_fss)
            self.fss.append(new_fs2)
            new_fs2.number = random.choice(fs_numbers)
            while new_fs2.number not in self.numbers_avail:
                new_fs2.number = random.choice(fs_numbers)
            fs_numbers.remove(int(new_fs2.number))
            self.numbers_avail.remove(int(new_fs2.number))
            print("FS " + new_fs2.full_name + ", #" + str(new_fs2.number) + " signed.")
            remaining_fa_fss = [Player for Player in fa_fss if Player.full_name != new_fs1.full_name
                            or Player.full_name != new_fs2.full_name]
        free_agents.extend(remaining_fa_fss)
            
    def sign_sss(self,Player):
        global free_agents
        fa_sss = [Player for Player in free_agents if Player.position == "ss"]
        free_agents = [Player for Player in free_agents if Player not in fa_sss]
        remaining_fa_sss = fa_sss
        ss_numbers = list(range(1,50))
        if len(self.sss) == 0:
            new_ss1 = random.choice(fa_sss)
            self.sss.append(new_ss1)
            new_ss1.number = random.choice(ss_numbers)
            while new_ss1.number not in self.numbers_avail:
                new_ss1.number = random.choice(ss_numbers)
            ss_numbers.remove(int(new_ss1.number))
            self.numbers_avail.remove(int(new_ss1.number))
            print("SS " + new_ss1.full_name + ", #" + str(new_ss1.number) + " signed.")

        if len(self.sss) == 1:
            new_ss2 = random.choice(fa_sss)
            while new_ss2.full_name == new_ss1.full_name:
                new_ss2 = random.choice(fa_sss)
            self.sss.append(new_ss2)
            new_ss2.number = random.choice(ss_numbers)
            while new_ss2.number not in self.numbers_avail:
                new_ss2.number = random.choice(ss_numbers)
            ss_numbers.remove(int(new_ss2.number))
            self.numbers_avail.remove(int(new_ss2.number))
            print("SS " + new_ss2.full_name + ", #" + str(new_ss2.number) + " signed.")
            remaining_fa_sss = [Player for Player in fa_sss if Player.full_name != new_ss1.full_name
                            or Player.full_name != new_ss2.full_name]
        free_agents.extend(remaining_fa_sss)

    def sign_p(self,Player):
        global free_agents
        fa_ps = [Player for Player in free_agents if Player.position == "p"]
        free_agents = [Player for Player in free_agents if Player not in fa_ps]
        remaining_fa_ps = fa_ps
        p_numbers = list(range(1,100))
        if len(self.ps) == 0:
            new_p1 = random.choice(fa_ps)
            self.ps.append(new_p1)
            new_p1.number = random.choice(p_numbers)
            while new_p1.number not in self.numbers_avail:
                new_p1.number = random.choice(p_numbers)
            p_numbers.remove(int(new_p1.number))
            self.numbers_avail.remove(int(new_p1.number))
            print("P " + new_p1.full_name + ", #" + str(new_p1.number) + " signed.")
            remaining_fa_ps = [Player for Player in fa_ps if Player.full_name is not new_p1.full_name]
        free_agents.extend(remaining_fa_ps)

    def sign_k(self,Player):
        global free_agents
        fa_ks = [Player for Player in free_agents if Player.position == "k"]
        free_agents = [Player for Player in free_agents if Player not in fa_ks]
        remaining_fa_ks = fa_ks
        k_numbers = list(range(1,100))
        if len(self.ks) == 0:
            new_k1 = random.choice(fa_ks)
            self.ks.append(new_k1)
            new_k1.number = random.choice(k_numbers)
            while new_k1.number not in self.numbers_avail:
                new_k1.number = random.choice(k_numbers)
            k_numbers.remove(int(new_k1.number))
            self.numbers_avail.remove(int(new_k1.number))
            print("K " + new_k1.full_name + ", #" + str(new_k1.number) + " signed.")
            remaining_fa_ks = [Player for Player in fa_ks if Player.full_name is not new_k1.full_name]
        free_agents.extend(remaining_fa_ks)
            
    def sign_ls(self,Player):
        global free_agents
        fa_lss = [Player for Player in free_agents if Player.position == "ls"]
        free_agents = [Player for Player in free_agents if Player not in fa_lss]
        remaining_fa_lss = fa_lss
        ls_numbers = list(range(1,100))
        if len(self.lss) == 0:
            new_ls1 = random.choice(fa_lss)
            self.lss.append(new_ls1)
            new_ls1.number = random.choice(ls_numbers)
            while new_ls1.number not in self.numbers_avail:
                new_ls1.number = random.choice(ls_numbers)
            ls_numbers.remove(int(new_ls1.number))
            self.numbers_avail.remove(int(new_ls1.number))
            print("LS " + new_ls1.full_name + ", #" + str(new_ls1.number) + " signed.")
            remaining_fa_lss = [Player for Player in fa_lss if Player.full_name is not new_ls1.full_name]
        free_agents.extend(remaining_fa_lss)

def create_rosters():
    global rosters
    while len(rosters) < 32:
        roster_count = len(rosters)
        rosters.append(Roster([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]))

def fill_rosters():
    global rosters
    ticker = 0
    while ticker <= 31:
        print("Team " + str(ticker) + " Drafting: ")
        rosters[ticker].sign_qbs(rosters[ticker])
        rosters[ticker].sign_hbs(rosters[ticker])
        rosters[ticker].sign_fbs(rosters[ticker])
        rosters[ticker].sign_tes(rosters[ticker])
        rosters[ticker].sign_wrs(rosters[ticker])
        rosters[ticker].sign_lts(rosters[ticker])
        rosters[ticker].sign_lgs(rosters[ticker])
        rosters[ticker].sign_cs(rosters[ticker])
        rosters[ticker].sign_rgs(rosters[ticker])
        rosters[ticker].sign_rts(rosters[ticker])
        rosters[ticker].sign_les(rosters[ticker])
        rosters[ticker].sign_res(rosters[ticker])
        rosters[ticker].sign_dts(rosters[ticker])
        rosters[ticker].sign_edges(rosters[ticker])
        rosters[ticker].sign_lolbs(rosters[ticker])
        rosters[ticker].sign_rolbs(rosters[ticker])
        rosters[ticker].sign_mlbs(rosters[ticker])
        rosters[ticker].sign_cbs(rosters[ticker])
        rosters[ticker].sign_fss(rosters[ticker])
        rosters[ticker].sign_sss(rosters[ticker])
        rosters[ticker].sign_p(rosters[ticker])
        rosters[ticker].sign_k(rosters[ticker])
        rosters[ticker].sign_ls(rosters[ticker])
        create_free_agents()
        ticker = ticker + 1
    ticker = 0

def order_depth_chart():
    global rosters
    ticker = 0
    while ticker <= 31:
        rosters[ticker].qbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].hbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].fbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].tes.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].wrs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].lts.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].lgs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].cs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].rgs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].rts.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].les.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].res.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].dts.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].edges.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].lolbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].rolbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].mlbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].cbs.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].fss.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].sss.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].ps.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].ks.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        rosters[ticker].lss.sort(key=lambda Player:Player.ovr_rating,reverse=True)
        ticker = ticker + 1
    ticker = 0


def update_playerbase():
    create_free_agents()
    create_rosters()
    fill_rosters()
    order_depth_chart()