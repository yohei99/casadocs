#
# stub function definition file for docstring parsing
#

def vishead(vis, mode='summary', listitems=['telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date'], hdkey='', hdindex='', hdvalue=''):
    r"""
List, summary, get, and put metadata in a measurement set

Parameters
   - **vis** (string) - Name of input visibility file
   - **mode** (string) - Mode of operation for vishead

Subparameters
   .. raw:: html

      <details><summary><i> mode = list </i></summary>

   - **listitems** (stringArray=
           ) - Keyword items to list. This parameter is only relevant in list mode. Note that the default list is a subset of the possible keywords. To get all the keywords set listitems=[]

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> mode = get </i></summary>

   - **hdkey** (string='') - Keyword to get/put
   - **hdindex** (string='') - Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> mode = put </i></summary>

   - **hdkey** (string='') - Keyword to get/put
   - **hdindex** (string='') - Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements
   - **hdvalue** (variant='') - Value of the keywords to be put in the MS (used in put mode only)

   .. raw:: html

      </details>


Description
      |         This task allows the user to manipulate some meta-data
        keywords in a measurement set. The mode='list' shows those
        keywords that are presently implemented, with their values. The
        contents associated with the keywords can be obtained with
        mode='get' and changed with mode='put'.
      |         The modes that are available are:

      -  list: List all keywords that are recognized, and list the
         value(s) for each.  Only these keywords can be obtained (get)
         or changed (put)
      -  summary: Provides a summary that is equivalent to running
         listobs(verbose=False)
      -  get: Get the specified keyword value(s) from the ms
      -  put: Put the specified keyword value(s) into the ms

              Keywords currently implemented are:

      -  cal_grp             
      -  field (Field names)
      -  fld_code (Field Observing codes)
      -  freq_group_name      
      -  log                  
      -  observer(Observer name)
      -  project (Project name)
      -  ptcs(Phase tracking centers for each field)
      -  release_date
      -  schedule
      -  schedule_type
      -  spw_name              
      -  source_name         
      -  telescope (Telescope Name)

      |         Note that the default list of keywords is a subset of
        the former list. To get
      |         all the keywords mentioned above set listitemts=[]. See
        the Parameter pages of vishead for more details.

      More information can also be found in the CASA Docs pages on
      `Listing and Changing MS
      Metadata <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/listing-and-manipulating-ms-metadata>`__.

    """
    pass
