


cdef extern from "bmi.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_sedflux3d(BMI_Model *model)
    BMI_Model* register_bmi_avulsion(BMI_Model *model)
    BMI_Model* register_bmi_plume(BMI_Model *model)
    BMI_Model* register_bmi_subside(BMI_Model *model)

