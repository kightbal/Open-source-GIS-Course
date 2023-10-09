from  gdal import  ogr
import  pandas as pd
import os
def read_shapefile(file_path,property_show=True,head_show=5):
    datasource=ogr.Open(file_path,0)
    layer=datasource.GetLayer()
    n_feature=layer.GetFeatureCount()
    n_filed=layer.GetFeature(0).GetFieldCount()
    property_table=list()
    field_name=list()
    for i in range(n_filed):
        field_name.append(layer.GetFeature(0).GetFiledDefnRef(i).name)
    for i in range(n_feature):
        fea=layer.GetFeature(i)
        property_fea=list()
        for j in range(n_filed):
            field=fea.GetField(j)
            property_fea.append(field)
        property_table.append(property_fea)
    df=pd.DataFrame(property_table,columns=field_name)
    if(property_show==False):
        datasource=None
        return layer
    df.head(head_show)
    datasource=None
    return layer

def write_shapefile(out_path,layer,filetype):
    n_infield=layer.GetFieldCount()
    n_infeature=layer.GetFeatureCount()
    driver=ogr.GetDriverByName("ESRI Shapefile")
    datasource=driver.CreateDataSource(out_path)
    layer_name=os.path.basename(out_path)
    out_layer=datasource.CreateLayer(layer_name,geom_type=filetype,
                                     srs=layer.GetSpatialRefrence())
    out_feature_defn=out_layer.GetLayerDefn()
    for i in range(n_infield):
        field_defn = layer.GetFeature(0).GetFiledDefn(i)
        out_layer.CreateField(field_defn)
    for i in range(n_infeature):
        in_feature=layer.GetFeature(i)
        in_geo=in_feature.GetGeometry()
        out_feature=ogr.Feature(out_feature_defn)
        out_feature.SetGeometry(in_geo)
        for j in range(n_infield):
            fieldvalue=in_feature.GetField(j)
            out_feature.SetField2(j,fieldvalue)
        out_layer.CreateFeature(out_feature)
    datasource=None
