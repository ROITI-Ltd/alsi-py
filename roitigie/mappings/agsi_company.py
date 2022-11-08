import enum


class AGSICompany(enum.Enum):
    """ENUM containing 2 things about an Area: code, country"""

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, country: str):
        """Constructor for the AGSICompany enum

        Parameters
        ----------
        country : str
            country string parameter needed for the lookup
        """
        self._country = country

    def __str__(self):
        return self.value

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            "country": self.country,
            "company": self.code,
        }

    astora = "21X000000001160J", "AT"
    gsa = "25X-GSALLC-----E", "AT"
    omv_gas_storage = "25X-OMVGASSTORA5", "AT"
    rag_energy_storage = "23X----100225-1C", "AT"
    uniper_energy_storage_at = "21X000000001127H", "AT"
    fluxys = "21X-BE-A-A0A0A-Y", "BE"
    bulgartransgaz = "21X-BG-A-A0A0A-C", "BG"
    psp = "31X-PSP-OSS-HR-D", "HR"
    mnd_energy_storage = "27XG-MNDGS-CZ--R", "CZ"
    moravia_gas_storage = "27X-MORAVIAGS--E", "CZ"
    rwe_gas_storage_cz = "27XG-RWE-GAS-STI", "CZ"
    spp_storage = "27X-SPPSTORAGE-R", "CZ"
    gsd = "21X000000001104T", "DK"
    storengy = "21X000000001083B", "FR"
    terega = "21X-FR-B-A0A0A-J", "FR"
    astora_germany = "21X000000001160J", "DE"
    bayernugs = "37X0000000000151", "DE"
    bes = "37X0000000000224", "DE"
    edf_gas_deutschland = "37X000000000152S", "DE"
    enbw_etzel_speicher = "11X0-0000-0667-8", "DE"
    eneco_gasspeicher = "21X0000000010849", "DE"
    enovos_storage = "**TOBEPROVIDED**", "DE"
    equinor_storage_deutschland = "21X000000001368W", "DE"
    erdgasspeicher_peissen = "21X000000001297T", "DE"
    ekb = "21X000000001080H", "DE"
    ewe_gasspeicher = "21X0000000011756", "DE"
    hansewerk = "21X0000000013805", "DE"
    kge = "21X000000001140P", "DE"
    met_speicher = "37X000000000047P", "DE"
    mnd_energy_storage_germany = "37X000000000042Z", "DE"
    n_ergie = "11XNERGIE------1", "DE"
    nafta_speicher_inzenham = "21X0000000011748", "DE"
    nuon_epe_gasspeicher = "37X0000000000119", "DE"
    omv_gas_storage_germany = "25X-OMVGASSTORA5", "DE"
    rwe_gas_storage_west = "21X000000001262B", "DE"
    stadtwerke_hannover = "11XSWHANNOVERAG3", "DE"
    storengy_deutschland = "21X000000001072G", "DE"
    swb_vertrieb_bremen = "11XSWB-BREMEN--I", "DE"
    swkiel_speicher = "37X000000000051Y", "DE"
    tep = "21X000000001307F", "DE"
    total_etzel_gaslager = "**TOBEPROVIDED**", "DE"
    trianel_gasspeicher_epe = "21X000000001310Q", "DE"
    uniper_energy_storage = "21X000000001127H", "DE"
    vng_gasspeicher_gmbh = "21X000000001138C", "DE"
    hexum = "21X0000000013643", "HU"
    hgs = "21X0000000013635", "HU"
    kinsale_energy = "47X0000000000584", "IE"
    edison_stoccaggio = "21X0000000013651", "IT"
    igs = "59X4-IGSTORAGE-T", "IT"
    stogit = "21X000000001250I", "IT"
    conexus_baltic_grid = "21X000000001379R", "LV"
    energystock = "21X000000001057C", "NL"
    ewe_gasspeicher_nl = "21X0000000011756", "NL"
    nam = "21X000000001075A", "NL"
    taqa_gas_storage = "21X000000001120V", "NL"
    taqa_piek_gas = "21X0000000013732", "NL"
    gsp = "53XPL000000OSMP5", "PL"
    ren_armazenagem = "21X0000000013627", "PT"
    depomures = "21X000000001300T", "RO"
    depogaz_ploiesti = "21X-DEPOGAZ-AGSI", "RO"
    nafta = "42X-NAFTA-SK---U", "SK"
    pozagas = "42X-POZAGAS-SK-V", "SK"
    enagas_gts = "21X0000000013368", "ES"
    swedegas = "21X-SE-A-A0A0A-F", "SE"
    centrica_storage = "21X000000001022V", "GB"
    edf = "23X-EDFE-------W", "GB"
    humbly_grove_energy = "55XHUMBLYGROVE1H", "GB"
    scottish_power = "23XSCOTTISHPOWEF", "GB"
    sse_gas_storage = "23X--140207-SSE9", "GB"
    storengy_uk = "48XSTORENGYUK01P", "GB"
    uniper_energy_storage_ltd = "21X0000000013716", "GB"
