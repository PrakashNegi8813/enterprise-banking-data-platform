from framework.context import create_context
from framework.metadata_reader import get_metadata
from framework.exception_handler import handle_exception

from src.bronze_loader import load_bronze
from src.silver_loader import load_silver
from src.gold_loader import load_gold


LOADER_MAPPING = {
    "BRONZE": load_bronze,
    "SILVER": load_silver,
    "GOLD": load_gold
}


def run_pipeline(spark, dataset):

    context = create_context(dataset)

    print("=" * 80)
    print(f"Starting Pipeline : {dataset}")
    print(f"Batch ID          : {context['batch_id']}")
    print("=" * 80)

    layers = ["BRONZE", "SILVER", "GOLD"]

    for layer in layers:

        print(f"\nExecuting {layer} Layer...")

        metadata = get_metadata(
            spark,
            dataset,
            layer
        )

        loader = LOADER_MAPPING[layer]

        try:

            loader(
                spark=spark,
                dataset=dataset,
                context=context,
                metadata=metadata
            )

            print(f"{layer} Completed Successfully")

        except Exception as ex:

            print(f"{layer} Failed")

            handle_exception(
                spark=spark,
                dataset=dataset,
                layer=layer,
                batch_id=context["batch_id"],
                ex=ex
            )

            raise

    print("\nPipeline Completed Successfully")
    print("=" * 80)

    return context["batch_id"]