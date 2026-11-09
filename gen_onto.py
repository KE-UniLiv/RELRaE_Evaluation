from relrae import RELRaE
import configparser
from pathlib import Path

def run_pipeline(pipeline, modules):
    print(modules)
    if modules[0] != "RuBREx":
        print("RuBREx is a required 1st module, errors are likely")
    for m in modules:
        print(f"Running {m}...")
        getattr(pipeline, m)()

components_root = Path("relrae_components")
cfg = configparser.ConfigParser()
config_path = components_root / "config" / "pipeline_conf.txt"

if not cfg.read(config_path):
    raise FileNotFoundError(f"Pipeline configuration not found: {config_path}")

modules = [
    module.strip()
    for module in cfg["MAIN"]["modules"].split(",")
    if module.strip()
]
schema = cfg["MAIN"]["schema"]
namespace = cfg["MAIN"]["namespace"]
prefix = cfg["MAIN"]["prefix"]
ontology_name = cfg["MAIN"]["ontology_name"]
pipeline = RELRaE(
    ontology_name,
    schema,
    namespace,
    prefix,
    cfg["MAIN"],
    components_root=components_root,
    output_root=components_root / "output"
)
run_pipeline(pipeline, modules)
pipeline.serialise()

print("PIPELINE COMPLETE")
