import sys, os, ast
import matplotlib.pyplot as plt
from lightcurve import lightcurve
from spectra import spectra
import warnings
warnings.filterwarnings("ignore")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        if len(sys.argv) == 2:  # If only one argument is provided
            erosita_downloader = lightcurve(target_name=sys.argv[1], radius=0.016)  # Set default radius or adjust accordingly
            erosita_downloader_ = spectra(target_name=sys.argv[1], radius=0.016)  # Set default radius or adjust accordingly
        elif len(sys.argv) == 3:  # If two arguments are provided
            erosita_downloader = lightcurve(ra=sys.argv[1], dec=sys.argv[2], radius=0.016)  # Set default radius or adjust accordingly
            erosita_downloader_ = spectra(ra=sys.argv[1], dec=sys.argv[2], radius=0.016)  # Set default radius or adjust accordingly
        else:
            raise ValueError("Invalid number of arguments. Please provide either target_name={str} or ra={float}, dec={float}.")

        xml_data = erosita_downloader.cone_search()
        xml_data_ = erosita_downloader_.cone_search()

        detuid = erosita_downloader.parse_xml_data(xml_data)
        detuid_ = erosita_downloader_.parse_xml_data(xml_data_)


        if detuid and detuid_:
            download_url = "https://erosita.mpe.mpg.de/dr1/erodat/data/download_source/{}".format(detuid)
            fn_dir = os.path.join(os.path.expanduser('~'), '.eROSITAViz')
            product_dir = os.path.join(fn_dir, 'data_products')
            file_name = "{}".format(detuid)
            fits_path = erosita_downloader.download_file(download_url, file_name, product_dir)

            download_url_ = "https://erosita.mpe.mpg.de/dr1/erodat/data/download_source/{}".format(detuid_)
            fn_dir_ = os.path.join(os.path.expanduser('~'), '.eROSITAViz')
            product_dir_ = os.path.join(fn_dir_, 'data_products')
            file_name_ = "{}".format(detuid_)
            fits_path_ = erosita_downloader_.download_file(download_url_, file_name_, product_dir_)

            erosita_downloader.plotter(fits_path)
            erosita_downloader_.plotter(fits_path_[0],fits_path_[1])
            plt.show()

    else:
        raise ValueError("Invalid number of arguments. Please provide either target_name={str} or ra={float}, dec={float}.")
