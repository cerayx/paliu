#Processing Automatic Location Identification Updates
##BS-SDI

What is BS-SDI? The BellSouth Standard Data Interface was developed as a standard procedure to get an 9-1-1 customer's records from the remote ALI database into an on-site retrieval system. It includes a method for electronically downloading the initial database load, and for the customer to get nightly service. order updates for their system.

###BS-SDI Load/Update Data Record Header
|Position|Length|Field             |Valid Values   |Description                                      |
|--------|------|------------------|---------------|-------------------------------------------------|
|001-003 |  3   |Header Entry      |UHL            |Constant value of UHL                            |
|004-005 |  2   |Filler            |Spaces         |Space filled                                     |
|006-011 |  6   |File Date         |Numeric        |Extract date of update or load file MMDDYY format|
|012-61  |  50  |Company Name      |BELLSOUTH      |Constant value of  BELLSOUTH                     |
|062-067 |  6   |Cycle Number      |Numeric        |Right justified, zero filled cycle number        |
|068-239 |  172 |Filler            |Spaces         |Space filled                                     |
|240     |  1   |End of Record     |Spaces         |Space filled                                     |
|241     |  1   |New Line Character|ASCII Code = 10|New Line Character                               |

###BS-SDI Load/Update Data Record Footer
|Position|Length|Field             |Valid Values   |Description                                      |
|--------|------|------------------|---------------|-------------------------------------------------|
|001-003 |  3   |Header Entry      |UTL            |Constant value of UTL                            |
|004-005 |  2   |Filler            |Spaces         |Space filled                                     |
|006-011 |  6   |File Date         |Numeric        |Extract date of update or load file MMDDYY format|
|012-61  |  50  |Company Name      |BELLSOUTH      |Constant value of BELLSOUTH                      |
|062-070 |  9   |Update/Load Count |Numeric        |Right justified, zero filled count               |
|071-239 |  169 |Filler            |Spaces         |Space filled                                     |
|240     |  1   |End of Record     |Spaces         |Space filled                                     |
|241     |  1   |New Line Character|ASCII Code = 10|New Line Character                               |

###BS-SDI Load/Update Data Record 
|Position|Length|Field             |Valid Values   |Description                                                |
|--------|------|------------------|---------------|-----------------------------------------------------------|
|001     |  1   |FOC               |I, D, or C     |Function of change code; I = Insert, D = Delete, C = Change|
|002-011 |  10  |Telephone Number  |Numeric|    10 digit TN to be updated| 
|012-021 |  10  |House Number      |Numeric|    Left justified house number|     
|022-025 |  4   |House Number SFX  |Alphanumeric|   Left justified House Number suffix|  
|026-027 |  2   |Street Dir Prefix |E,W,N,S,NW,NE,SW, SE or Spaces| Left justified street directional prefix or spaces if no prefix|     
|028-067 |  40  |Street Name       |Alphanumeric|   Left justified Street name including thoroughfare and post directional|  
|068-073 |  6   |Filler            |Spaces     |Space filled|
|074-105 |  32  |Community Name    |Alphanumeric|   Left justified Community Name|
|106-107 |  2   |State             |AL MS NC SC TN| State abbreviation|
|108-127 |  20  |Location          |Alphanumeric|   Left justified additional street information describing location of caller or spaces|
|128-159|   32| Customer Name|  Alphanumeric|   Left justified name of customer|     
|160|   1|  Class of Service|   0-9, A-G|   Class of Service Values 0 = DPA Business, 1 = Residential service, 2 = Business service, 3 = Residential PBX service, 4 = Business PBX service,  5 = Centrex/ESSX service, 6 = Semi-public coin service, 7 = Public coin service, 8 = Mobile, 9 = DPA Residence, A = Outdial Semi-public Coin, B = Outdial Public, C = ALEC business customer, D = ALEC residence customer, E = ALEC public customer, F = ALEC Outdial public customer, G = Wireless|
|161|   1|  Type of Service|    0-9|Type of Service Values  0 = Non pub nor FX, 1= FX not non-pub 3 = Non pub, 4 = non pub and FX, 8 = PinPoint published, 9 = PinPoint non pub|
|162-165|   4|  Exchange|   Alphanumeric|   Left justified wire center exchange|
|166-168|   3|  ALI ESN|    Numeric 3 character| Emergency Service Number|   
|169-170|   2|  Filler| Spaces| Space filled    | 
|171-180|   10| Main Number|    Numeric|    10 digit Main billing Number|    
|181-187|   7|  Service Order Number|   Alphanumeric|   Left justified Service Order number|
|188-190|   3|  Filler| Spaces| Space filled|
|191-196|   6|  Change Date|    Numeric|    Date record was last modified (MMDDYY format)|   
|197-200|   4|  MSAG Customer ID|   Alphanumeric|   Left justified MSAG Customer ID | 
|201-205|   5|  Company ID| Alphanumeric|   Left justified NENA Company ID  | 
|206-239|   34| Filler| Spaces| Space filled|    
|240    |1| End of Record|  Spaces| Space filled|    
|241|   1|  New Line Character| ASCII Code = 10|    New Line Character |    