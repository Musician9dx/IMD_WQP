#----------------------------------------------------------------
# Generated CMake target import file for configuration "RELEASE".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ArrowDataset::arrow_dataset_shared" for configuration "RELEASE"
set_property(TARGET ArrowDataset::arrow_dataset_shared APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ArrowDataset::arrow_dataset_shared PROPERTIES
  IMPORTED_IMPLIB_RELEASE "D:/INeuron/IMD_WQP/environment/Library/arrow_dataset.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/arrow_dataset.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ArrowDataset::arrow_dataset_shared )
list(APPEND _IMPORT_CHECK_FILES_FOR_ArrowDataset::arrow_dataset_shared "D:/INeuron/IMD_WQP/environment/Library/arrow_dataset.lib" "${_IMPORT_PREFIX}/bin/arrow_dataset.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
