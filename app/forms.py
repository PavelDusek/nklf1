from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    SelectField,
    BooleanField,
    FloatField,
    TextAreaField,
    SubmitField,
)


class KultivaceForm(FlaskForm):
    text = TextAreaField("Výsledky kultivací:")
    submit = SubmitField("Převést")


class BilanceForm(FlaskForm):
    # reg = TextAreaField(u"Regulární výraz pro vyhledání bilancí:", default=u"[Bb]ilance\s*tekutin\s*\(?P\/V\)?:?\s*(\d+)\s*\/\s*(\d+)")
    spli = TextAreaField(
        "Regulární výraz pro hranici dnů:", default=r"------  Dokumentace ze"
    )
    reg = TextAreaField(
        "Regulární výraz pro vyhledání bilancí:",
        default=r"[Bb]ilance\s*\w*\s*\(?P\/V\)?:?\s*\+?(\d+)\s*\/\s*-?(\d+)",
    )
    temp = TextAreaField(
        "Regulární výraz pro teplotu:", default=r"TT:?\s*(\d+)[\.,]?(\d+)?\s*(°C|st)"
    )
    dat = TextAreaField(
        "Regulární výraz pro datum:", default=r"dne (\d+\.\d+\.\d+) ---------:"
    )
    text = TextAreaField(
        "Text dekurzů:",
        default="""------  Dokumentace ze dne 03.03.21 ---------:
TT 38 st, TK  120/80 , TF 88/min, eupnoe, SpO2 73% nativně, 83% na  10l/min O2 maskou, při HFNO 90 l/min na  100% Fi02 , bilance tekutin (P/V): 4020/1500 ml/24h

------  Dokumentace ze dne 04.03.21 ---------:
      DEKURZ ze dne 04.03.21
TT 37,2st, TK  110/65 , TF 89/min, eupnoe, SpO2 86 při HFNO 90 l/min na  100% Fi02 , DF 28/min, CVP ?, bilance tekutin (P/V): 3422/600 ml/24h

------  Dokumentace ze dne 05.03.21 ---------:
      DEKURZ ze dne 05.03.21
Objektivně somaticky: TT 37,6 °C, TK 134/61 mm Hg, TF 82/min, DF: 31/min., SpO2 90 při NIV FiO2 75 % + PEEP 10, bilance tekutin P/V: 4076/3500 ml/24 hod.""",
    )
    submit = SubmitField("Vyhledat bilance")


class LaborForm(FlaskForm):
    text = TextAreaField("Výsledky laboratoře:")
    submit = SubmitField("Převést")


class SonoForm(FlaskForm):
    tcd = BooleanField("TCD", default=True)

    machine = SelectField(
        "přístroj",
        choices=[
            ("Canon Aplio a", "Canon Aplio a"),
            ("Canon Aplio go", "Canon Aplio go"),
            ("Canon Aplio i800", "Canon Aplio i800"),
            ("Toshiba 4D Aplio 300", "Toshiba 4D Aplio 300"),
        ],
    )

    kvalita = SelectField(
        "celková kvalita obrazu",
        choices=[
            ("excelentní", "excelentní"),  # 1
            ("dobrá", "dobrá"),  # 2
            ("adekvátní", "adekvátní"),  # 3
            ("špatná", "špatná"),  # 4
            ("nediagnostická", "nediagnostická"),  # 5
        ],
    )

    vyteznost = SelectField(
        "diagnostická výtěžnost",
        choices=[
            ("excelentní", "excelentní"),  # 1
            ("dobrá", "dobrá"),  # 2
            ("nedostatečná", "nedostatečná"),  # 3
        ],
    )

    year = IntegerField("rok narozeni")
    vji = BooleanField("VJI kompresibilní", default=True)
    thyroid = BooleanField("Štítnice homogenní", default=True)
    heart_rhytm = BooleanField("Srdeční akce pravidelná", default=True)

    # sin
    imt_sn_max = FloatField("ACC sin IMT max.")
    imt_sn_mean = FloatField("ACC sin IMT mean.")

    acc_sn_plaq_width = FloatField("pláty vlevo tloušťka")
    acc_sn_plaq_echo = SelectField(
        "pláty vlevo echogenita",
        choices=[
            ("hypoechogennní", "hypoechogennní"),
            ("isoechogenní", "isoechogenní"),
            ("hyperechogenní", "hyperechogenní"),
            ("smíšený", "smíšený"),
        ],
    )
    acc_sn_plaq_surf = SelectField(
        "pláty vlevo povrch",
        choices=[("hladký", "hladký"), ("nerovný", "nerovný")],
    )

    aci_sn_laminar = BooleanField("ACI sin laminar", default=True)

    acc_sn_psv = IntegerField("ACC sin PSV")
    acc_sn_vm = IntegerField("ACC sin Vm")
    acc_sn_edv = IntegerField("ACC sin EDV")
    acc_sn_pi = FloatField("ACC sin PI")
    acc_sn_ri = FloatField("ACC sin RI")
    acc_sn_mm = FloatField("ACC sin mm")

    aci_sn_prox_psv = IntegerField("ACI sin prox PSV")
    aci_sn_prox_vm = IntegerField("ACI sin prox Vm")
    aci_sn_prox_edv = IntegerField("ACI sin prox EDV")
    aci_sn_prox_pi = FloatField("ACI sin prox PI")
    aci_sn_prox_ri = FloatField("ACI sin prox RI")
    aci_sn_prox_mm = FloatField("ACI sin prox mm")

    aci_sn_dist_psv = IntegerField("ACI sin dist PSV")
    aci_sn_dist_vm = IntegerField("ACI sin dist Vm")
    aci_sn_dist_edv = IntegerField("ACI sin dist EDV")
    aci_sn_dist_pi = FloatField("ACI sin dist PI")
    aci_sn_dist_ri = FloatField("ACI sin dist RI")
    aci_sn_dist_mm = FloatField("ACI sin dist mm")

    aci_sn_sub_psv = IntegerField("ACI sin sub PSV")
    aci_sn_sub_vm = IntegerField("ACI sin sub Vm")
    aci_sn_sub_edv = IntegerField("ACI sin sub EDV")
    aci_sn_sub_pi = FloatField("ACI sin sub PI")
    aci_sn_sub_ri = FloatField("ACI sin sub RI")
    aci_sn_sub_mm = IntegerField("ACI sin sub mm")

    ace_sn_psv = IntegerField("ACE sin PSV")
    ace_sn_vm = IntegerField("ACE sin Vm")
    ace_sn_edv = IntegerField("ACE sin EDV")
    ace_sn_pi = FloatField("ACE sin PI")
    ace_sn_ri = FloatField("ACE sin RI")
    ace_sn_mm = FloatField("ACE sin mm")

    sub_sn_psv = IntegerField("Subclavia sin PSV")
    sub_sn_vm = IntegerField("Subclavia sin Vm")
    sub_sn_edv = IntegerField("Subclavia sin EDV")
    sub_sn_pi = FloatField("Subclavia sin PI")
    sub_sn_ri = FloatField("Subclavia sin RI")
    sub_sn_mm = FloatField("Subclavia sin mm")

    v0_sn_psv = IntegerField("V0 sin PSV")
    v0_sn_vm = IntegerField("V0 sin Vm")
    v0_sn_edv = IntegerField("V0 sin EDV")
    v0_sn_pi = FloatField("V0 sin PI")
    v0_sn_ri = FloatField("V0 sin RI")
    v0_sn_mm = FloatField("V0 sin mm")
    v1_sn_psv = IntegerField("V1 sin PSV")
    v1_sn_vm = IntegerField("V1 sin Vm")
    v1_sn_edv = IntegerField("V1 sin EDV")
    v1_sn_pi = FloatField("V1 sin PI")
    v1_sn_ri = FloatField("V1 sin RI")
    v1_sn_mm = FloatField("V1 sin mm")
    v2_sn_psv = IntegerField("V2 sin PSV")
    v2_sn_vm = IntegerField("V2 sin Vm")
    v2_sn_edv = IntegerField("V2 sin EDV")
    v2_sn_pi = FloatField("V2 sin PI")
    v2_sn_ri = FloatField("V2 sin RI")
    v2_sn_mm = FloatField("V2 sin mm")
    v3_sn_psv = IntegerField("V3 sin PSV")
    v3_sn_vm = IntegerField("V3 sin Vm")
    v3_sn_edv = IntegerField("V3 sin EDV")
    v3_sn_pi = FloatField("V3 sin PI")
    v3_sn_ri = FloatField("V3 sin RI")
    v3_sn_mm = FloatField("V3 sin mm")

    # dx
    imt_dx_max = FloatField("ACC dx IMT max.")
    imt_dx_mean = FloatField("ACC dx IMT mean.")
    acc_dx_plaq_width = FloatField("pláty vpravo tloušťka")
    acc_dx_plaq_echo = SelectField(
        "pláty vpravo echogenita",
        choices=[
            ("hypoechogennní", "hypoechogennní"),
            ("isoechogenní", "isoechogenní"),
            ("hyperechogenní", "hyperechogenní"),
            ("smíšený", "smíšený"),
        ],
    )
    acc_dx_plaq_surf = SelectField(
        "pláty vpravo povrch",
        choices=[("hladký", "hladký"), ("nerovný", "nerovný")],
    )

    aci_dx_laminar = BooleanField("ACI sin laminar", default=True)

    acc_dx_psv = IntegerField("ACC dx PSV")
    acc_dx_vm = IntegerField("ACC dx Vm")
    acc_dx_edv = IntegerField("ACC dx EDV")
    acc_dx_pi = FloatField("ACC dx PI")
    acc_dx_ri = FloatField("ACC dx RI")
    acc_dx_mm = FloatField("ACC dx mm")

    aci_dx_prox_psv = IntegerField("ACI dx prox PSV")
    aci_dx_prox_vm = IntegerField("ACI dx prox Vm")
    aci_dx_prox_edv = IntegerField("ACI dx prox EDV")
    aci_dx_prox_pi = FloatField("ACI dx prox PI")
    aci_dx_prox_ri = FloatField("ACI dx prox RI")
    aci_dx_prox_mm = FloatField("ACI dx prox mm")

    aci_dx_dist_psv = IntegerField("ACI dx dist PSV")
    aci_dx_dist_vm = IntegerField("ACI dx dist Vm")
    aci_dx_dist_edv = IntegerField("ACI dx dist EDV")
    aci_dx_dist_pi = FloatField("ACI dx dist PI")
    aci_dx_dist_ri = FloatField("ACI dx dist RI")
    aci_dx_dist_mm = FloatField("ACI dx dist mm")

    aci_dx_sub_psv = IntegerField("ACI dx sub PSV")
    aci_dx_sub_vm = IntegerField("ACI dx sub Vm")
    aci_dx_sub_edv = IntegerField("ACI dx sub EDV")
    aci_dx_sub_pi = FloatField("ACI dx sub PI")
    aci_dx_sub_ri = FloatField("ACI dx sub RI")
    aci_dx_sub_mm = IntegerField("ACI dx sub mm")

    ace_dx_psv = IntegerField("ACE dx PSV")
    ace_dx_vm = IntegerField("ACE dx Vm")
    ace_dx_edv = IntegerField("ACE dx EDV")
    ace_dx_pi = FloatField("ACE dx PI")
    ace_dx_ri = FloatField("ACE dx RI")
    ace_dx_mm = FloatField("ACE dx mm")

    sub_dx_psv = IntegerField("Subclavia dx PSV")
    sub_dx_psv = IntegerField("Subclavia dx PSV")
    sub_dx_vm = IntegerField("Subclavia dx Vm")
    sub_dx_edv = IntegerField("Subclavia dx EDV")
    sub_dx_pi = FloatField("Subclavia dx PI")
    sub_dx_ri = FloatField("Subclavia dx RI")
    sub_dx_mm = FloatField("Subclavia dx mm")

    v0_dx_psv = IntegerField("V0 dx PSV")
    v0_dx_vm = IntegerField("V0 dx Vm")
    v0_dx_edv = IntegerField("V0 dx EDV")
    v0_dx_pi = FloatField("V0 dx PI")
    v0_dx_ri = FloatField("V0 dx RI")
    v0_dx_mm = FloatField("V0 dx mm")
    v1_dx_psv = IntegerField("V1 dx PSV")
    v1_dx_vm = IntegerField("V1 dx Vm")
    v1_dx_edv = IntegerField("V1 dx EDV")
    v1_dx_pi = FloatField("V1 dx PI")
    v1_dx_ri = FloatField("V1 dx RI")
    v1_dx_mm = FloatField("V1 dx mm")
    v2_dx_psv = IntegerField("V2 dx PSV")
    v2_dx_vm = IntegerField("V2 dx Vm")
    v2_dx_edv = IntegerField("V2 dx EDV")
    v2_dx_pi = FloatField("V2 dx PI")
    v2_dx_ri = FloatField("V2 dx RI")
    v2_dx_mm = FloatField("V2 dx mm")
    v3_dx_psv = IntegerField("V3 dx PSV")
    v3_dx_vm = IntegerField("V3 dx Vm")
    v3_dx_edv = IntegerField("V3 dx EDV")
    v3_dx_pi = FloatField("V3 dx PI")
    v3_dx_ri = FloatField("V3 dx RI")
    v3_dx_mm = FloatField("V3 dx mm")

    # Ophthalmic
    ophth_sn_psv = IntegerField("Ophthalmic sin PSV")
    ophth_sn_vm = IntegerField("Ophthalmic sin Vm")
    ophth_sn_edv = IntegerField("Ophthalmic sin EDV")
    ophth_sn_pi = FloatField("Ophthalmic sin PI")
    ophth_sn_ri = FloatField("Ophthalmic sin RI")
    ophth_sn_mm = IntegerField("Ophthalmic sin hloubka")

    ophth_dx_psv = IntegerField("Ophthalmic dx PSV")
    ophth_dx_vm = IntegerField("Ophthalmic dx Vm")
    ophth_dx_edv = IntegerField("Ophthalmic dx EDV")
    ophth_dx_pi = FloatField("Ophthalmic dx PI")
    ophth_dx_ri = FloatField("Ophthalmic dx RI")
    ophth_dx_mm = IntegerField("Ophthalmic dx hloubka")

    # TCDS transtemporalni
    tm_sn_okno = BooleanField("Temporální okno vlevo", default=True)

    ACM_sn_psv = IntegerField("ACM sin PSV")
    ACM_sn_vm = IntegerField("ACM sin Vm")
    ACM_sn_edv = IntegerField("ACM sin EDV")
    ACM_sn_pi = FloatField("ACM sin PI")
    ACM_sn_ri = FloatField("ACM sin RI")
    ACM_sn_mm = IntegerField("ACM sin hloubka")

    ACM2_sn_psv = IntegerField("ACM 2 sin PSV")
    ACM2_sn_vm = IntegerField("ACM 2 sin Vm")
    ACM2_sn_edv = IntegerField("ACM 2 sin EDV")
    ACM2_sn_pi = FloatField("ACM 2 sin PI")
    ACM2_sn_ri = FloatField("ACM 2 sin RI")
    ACM2_sn_mm = IntegerField("ACM 2 sin hloubka")

    ACM3_sn_psv = IntegerField("ACM 3 sin PSV")
    ACM3_sn_vm = IntegerField("ACM 3 sin Vm")
    ACM3_sn_edv = IntegerField("ACM 3 sin EDV")
    ACM3_sn_pi = FloatField("ACM 3 sin PI")
    ACM3_sn_ri = FloatField("ACM 3 sin RI")
    ACM3_sn_mm = IntegerField("ACM 3 sin hloubka")

    ACA_sn_psv = IntegerField("ACA sin PSV")
    ACA_sn_vm = IntegerField("ACA sin Vm")
    ACA_sn_edv = IntegerField("ACA sin EDV")
    ACA_sn_pi = FloatField("ACA sin PI")
    ACA_sn_ri = FloatField("ACA sin RI")
    ACA_sn_mm = IntegerField("ACA sin hloubka")

    P1pre_sn_psv = IntegerField("P1 pre sin PSV")
    P1pre_sn_vm = IntegerField("P1 pre sin Vm")
    P1pre_sn_edv = IntegerField("P1 pre sin EDV")
    P1pre_sn_pi = FloatField("P1 pre sin PI")
    P1pre_sn_ri = FloatField("P1 pre sin RI")
    P1pre_sn_mm = IntegerField("P1 pre sin hloubka")

    P1post_sn_psv = IntegerField("P1 post sin PSV")
    P1post_sn_vm = IntegerField("P1 post sin Vm")
    P1post_sn_edv = IntegerField("P1 post sin EDV")
    P1post_sn_pi = FloatField("P1 post sin PI")
    P1post_sn_ri = FloatField("P1 post sin RI")
    P1post_sn_mm = IntegerField("P1 post sin hloubka")

    P2_sn_psv = IntegerField("P2 sin PSV")
    P2_sn_edv = IntegerField("P2 sin EDV")
    P2_sn_vm = IntegerField("P2 sin Vm")
    P2_sn_pi = FloatField("P2 sin PI")
    P2_sn_ri = FloatField("P2 sin RI")
    P2_sn_mm = IntegerField("P2 sin hloubka")

    tm_dx_okno = BooleanField("Temporální okno vpravo", default=True)

    ACM_dx_psv = IntegerField("ACM dx PSV")
    ACM_dx_vm = IntegerField("ACM dx Vm")
    ACM_dx_edv = IntegerField("ACM dx EDV")
    ACM_dx_pi = FloatField("ACM dx PI")
    ACM_dx_ri = FloatField("ACM dx RI")
    ACM_dx_mm = IntegerField("ACM dx hloubka")

    ACM2_dx_psv = IntegerField("ACM 2 dx PSV")
    ACM2_dx_vm = IntegerField("ACM 2 dx Vm")
    ACM2_dx_edv = IntegerField("ACM 2 dx EDV")
    ACM2_dx_pi = FloatField("ACM 2 dx PI")
    ACM2_dx_ri = FloatField("ACM 2 dx RI")
    ACM2_dx_mm = IntegerField("ACM 2 dx hloubka")

    ACM3_dx_psv = IntegerField("ACM 3 dx PSV")
    ACM3_dx_vm = IntegerField("ACM 3 dx Vm")
    ACM3_dx_edv = IntegerField("ACM 3 dx EDV")
    ACM3_dx_pi = FloatField("ACM 3 dx PI")
    ACM3_dx_ri = FloatField("ACM 3 dx RI")
    ACM3_dx_mm = IntegerField("ACM 3 dx hloubka")

    ACA_dx_psv = IntegerField("ACA dx PSV")
    ACA_dx_vm = IntegerField("ACA dx Vm")
    ACA_dx_edv = IntegerField("ACA dx EDV")
    ACA_dx_pi = FloatField("ACA dx PI")
    ACA_dx_ri = FloatField("ACA dx RI")
    ACA_dx_mm = IntegerField("ACA dx hloubka")

    P1pre_dx_psv = IntegerField("P1 pre dx PSV")
    P1pre_dx_vm = IntegerField("P1 pre dx Vm")
    P1pre_dx_edv = IntegerField("P1 pre dx EDV")
    P1pre_dx_pi = FloatField("P1 pre dx PI")
    P1pre_dx_ri = FloatField("P1 pre dx RI")
    P1pre_dx_mm = IntegerField("P1 pre dx hloubka")

    P1post_dx_psv = IntegerField("P1 post dx PSV")
    P1post_dx_vm = IntegerField("P1 post dx Vm")
    P1post_dx_edv = IntegerField("P1 post dx EDV")
    P1post_dx_pi = FloatField("P1 post dx PI")
    P1post_dx_ri = FloatField("P1 post dx RI")
    P1post_dx_mm = IntegerField("P1 post dx hloubka")

    P2_dx_psv = IntegerField("P2 dx PSV")
    P2_dx_vm = IntegerField("P2 dx Vm")
    P2_dx_edv = IntegerField("P2 dx EDV")
    P2_dx_pi = FloatField("P2 dx PI")
    P2_dx_ri = FloatField("P2 dx RI")
    P2_dx_mm = IntegerField("P2 dx hloubka")

    # TCDS transforaminalni
    V4_sn_psv = IntegerField("V4 sin PSV")
    V4_sn_vm = IntegerField("V4 sin Vm")
    V4_sn_edv = IntegerField("V4 sin EDV")
    V4_sn_pi = FloatField("V4 sin PI")
    V4_sn_ri = FloatField("V4 sin RI")
    V4_sn_mm = IntegerField("V4 sin hloubka")

    V4_dx_psv = IntegerField("V4 dx PSV")
    V4_dx_vm = IntegerField("V4 dx Vm")
    V4_dx_edv = IntegerField("V4 dx EDV")
    V4_dx_pi = FloatField("V4 dx PI")
    V4_dx_ri = FloatField("V4 dx RI")
    V4_dx_mm = IntegerField("V4 dx hloubka")

    AB_junkce = IntegerField("AB junkce")
    AB_psv = IntegerField("AB PSV")
    AB_vm = IntegerField("AB Vm")
    AB_edv = IntegerField("AB EDV")
    AB_pi = FloatField("AB PI")
    AB_ri = FloatField("AB RI")
    AB_mm = IntegerField("AB hloubka")

    ventricle3 = FloatField("3.komora")

    echo = BooleanField("ECHO")
    echo_lv_sys = SelectField(
        "Systolicka funkce LK",
        choices=[("dobrá", "dobrá"), ("hraniční", "hraniční"), ("snížená", "snížená")],
    )
    echo_ef = IntegerField("EF LK")
    echo_fs = IntegerField("Fractional shortening LK")
    echo_mapse = IntegerField("MAPSE")

    echo_lv_dia = SelectField(
        "Diastolicka funkce LK",
        choices=[
            ("normální", "normální"),
            ("charakteru poruchy relaxace", "charakteru poruchy relaxace"),
            ("charakteru pseudonormalizace", "charakteru pseudonormalizace"),
            ("s restriktivním plněním", "s restriktivním plněním"),
        ],
    )
    echo_ea = FloatField("E/A")

    echo_rv_sys = SelectField(
        "Systolicka funkce PK",
        choices=[("dobrá", "dobrá"), ("hraniční", "hraniční"), ("snížená", "snížená")],
    )
    echo_tapse = IntegerField("TAPSE")

    echo_dilatace = BooleanField("Srdecni oddily dilatovane")
    echo_lav = FloatField("LAV")
    echo_lavi = FloatField("LAVi")

    echo_co_interpretace = SelectField(
        "Srdecni vydej",
        choices=[("dobrý", "dobrý"), ("hraniční", "hraniční"), ("snížený", "snížený")],
    )
    echo_lvot_vti = IntegerField("LVOT VTI")
    echo_co = FloatField("CO")
    echo_ci = FloatField("CI")

    submit = SubmitField("Submit")
