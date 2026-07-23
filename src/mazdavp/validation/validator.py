from .results import ValidationReport

class ManifestValidator:

    def validate(self, manifest):
        report = ValidationReport()

        vehicle = manifest.vehicle

        if len(vehicle.msc.value) != 7:
            report.add_error("msc", "MSC must contain exactly 7 characters.")

        if not vehicle.model_year:
            report.add_error("model_year", "Model year is required.")

        if not vehicle.market:
            report.add_warning("market", "Market has not been supplied.")

        if not vehicle.trim:
            report.add_warning("trim", "Trim has not been supplied.")

        if not vehicle.colour:
            report.add_warning("colour", "Colour has not been supplied.")

        return report
