from os.path import join, abspath, dirname

from rasters import Raster, RasterGeometry

TOPT_FILENAME = join(abspath(dirname(__file__)), "chen_optimum_temperature_C.tif")

def load_chen_optimum_temperature_C(geometry: RasterGeometry = None) -> Raster:
    """
    Load the optimum temperature raster.

    Parameters
    ----------
    geometry : RasterGeometry, optional
        The geometry to which the raster should be transformed. If None, the original raster geometry is used.

    Returns
    -------
    Raster
        The loaded optimum temperature raster, potentially transformed to the given geometry.
    """
    Topt_C = Raster.open(TOPT_FILENAME)

    if geometry is not None:
        Topt_C = Topt_C.to_geometry(geometry)

    return Topt_C
    