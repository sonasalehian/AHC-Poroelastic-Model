# trace generated using paraview version 5.10.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Xdmf3ReaderT'
facet_tagsxdmf = Xdmf3ReaderT(registrationName='facet_tags.xdmf', FileName=['../output/AJ/facet_tags.xdmf'])
facet_tagsxdmf.PointArrays = []
facet_tagsxdmf.CellArrays = ['aquifersys_cells', 'aquifersys_facets']
facet_tagsxdmf.Sets = []

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
facet_tagsxdmfDisplay = Show(facet_tagsxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
facet_tagsxdmfDisplay.Selection = None
facet_tagsxdmfDisplay.Representation = 'Surface'
facet_tagsxdmfDisplay.ColorArrayName = [None, '']
facet_tagsxdmfDisplay.LookupTable = None
facet_tagsxdmfDisplay.MapScalars = 1
facet_tagsxdmfDisplay.MultiComponentsMapping = 0
facet_tagsxdmfDisplay.InterpolateScalarsBeforeMapping = 1
facet_tagsxdmfDisplay.Opacity = 1.0
facet_tagsxdmfDisplay.PointSize = 2.0
facet_tagsxdmfDisplay.LineWidth = 1.0
facet_tagsxdmfDisplay.RenderLinesAsTubes = 0
facet_tagsxdmfDisplay.RenderPointsAsSpheres = 0
facet_tagsxdmfDisplay.Interpolation = 'Gouraud'
facet_tagsxdmfDisplay.Specular = 0.0
facet_tagsxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.SpecularPower = 100.0
facet_tagsxdmfDisplay.Luminosity = 0.0
facet_tagsxdmfDisplay.Ambient = 0.0
facet_tagsxdmfDisplay.Diffuse = 1.0
facet_tagsxdmfDisplay.Roughness = 0.3
facet_tagsxdmfDisplay.Metallic = 0.0
facet_tagsxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.Anisotropy = 0.0
facet_tagsxdmfDisplay.AnisotropyRotation = 0.0
facet_tagsxdmfDisplay.BaseIOR = 1.5
facet_tagsxdmfDisplay.CoatStrength = 0.0
facet_tagsxdmfDisplay.CoatIOR = 2.0
facet_tagsxdmfDisplay.CoatRoughness = 0.0
facet_tagsxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.SelectTCoordArray = 'None'
facet_tagsxdmfDisplay.SelectNormalArray = 'None'
facet_tagsxdmfDisplay.SelectTangentArray = 'None'
facet_tagsxdmfDisplay.Texture = None
facet_tagsxdmfDisplay.RepeatTextures = 1
facet_tagsxdmfDisplay.InterpolateTextures = 0
facet_tagsxdmfDisplay.SeamlessU = 0
facet_tagsxdmfDisplay.SeamlessV = 0
facet_tagsxdmfDisplay.UseMipmapTextures = 0
facet_tagsxdmfDisplay.ShowTexturesOnBackface = 1
facet_tagsxdmfDisplay.BaseColorTexture = None
facet_tagsxdmfDisplay.NormalTexture = None
facet_tagsxdmfDisplay.NormalScale = 1.0
facet_tagsxdmfDisplay.CoatNormalTexture = None
facet_tagsxdmfDisplay.CoatNormalScale = 1.0
facet_tagsxdmfDisplay.MaterialTexture = None
facet_tagsxdmfDisplay.OcclusionStrength = 1.0
facet_tagsxdmfDisplay.AnisotropyTexture = None
facet_tagsxdmfDisplay.EmissiveTexture = None
facet_tagsxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.FlipTextures = 0
facet_tagsxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
facet_tagsxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.BackfaceOpacity = 1.0
facet_tagsxdmfDisplay.Position = [0.0, 0.0, 0.0]
facet_tagsxdmfDisplay.Scale = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
facet_tagsxdmfDisplay.Origin = [0.0, 0.0, 0.0]
facet_tagsxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
facet_tagsxdmfDisplay.Pickable = 1
facet_tagsxdmfDisplay.Triangulate = 0
facet_tagsxdmfDisplay.UseShaderReplacements = 0
facet_tagsxdmfDisplay.ShaderReplacements = ''
facet_tagsxdmfDisplay.NonlinearSubdivisionLevel = 1
facet_tagsxdmfDisplay.UseDataPartitions = 0
facet_tagsxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
facet_tagsxdmfDisplay.OSPRayScaleArray = ''
facet_tagsxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
facet_tagsxdmfDisplay.OSPRayMaterial = 'None'
facet_tagsxdmfDisplay.BlockSelectors = ['/']
facet_tagsxdmfDisplay.BlockColors = []
facet_tagsxdmfDisplay.BlockOpacities = []
facet_tagsxdmfDisplay.Orient = 0
facet_tagsxdmfDisplay.OrientationMode = 'Direction'
facet_tagsxdmfDisplay.SelectOrientationVectors = 'None'
facet_tagsxdmfDisplay.Scaling = 0
facet_tagsxdmfDisplay.ScaleMode = 'No Data Scaling Off'
facet_tagsxdmfDisplay.ScaleFactor = 350.0
facet_tagsxdmfDisplay.SelectScaleArray = 'None'
facet_tagsxdmfDisplay.GlyphType = 'Arrow'
facet_tagsxdmfDisplay.UseGlyphTable = 0
facet_tagsxdmfDisplay.GlyphTableIndexArray = 'None'
facet_tagsxdmfDisplay.UseCompositeGlyphTable = 0
facet_tagsxdmfDisplay.UseGlyphCullingAndLOD = 0
facet_tagsxdmfDisplay.LODValues = []
facet_tagsxdmfDisplay.ColorByLODIndex = 0
facet_tagsxdmfDisplay.GaussianRadius = 17.5
facet_tagsxdmfDisplay.ShaderPreset = 'Sphere'
facet_tagsxdmfDisplay.CustomTriangleScale = 3
facet_tagsxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
facet_tagsxdmfDisplay.Emissive = 0
facet_tagsxdmfDisplay.ScaleByArray = 0
facet_tagsxdmfDisplay.SetScaleArray = [None, '']
facet_tagsxdmfDisplay.ScaleArrayComponent = 0
facet_tagsxdmfDisplay.UseScaleFunction = 1
facet_tagsxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
facet_tagsxdmfDisplay.OpacityByArray = 0
facet_tagsxdmfDisplay.OpacityArray = [None, '']
facet_tagsxdmfDisplay.OpacityArrayComponent = 0
facet_tagsxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
facet_tagsxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
facet_tagsxdmfDisplay.SelectionCellLabelBold = 0
facet_tagsxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
facet_tagsxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.SelectionCellLabelFontFile = ''
facet_tagsxdmfDisplay.SelectionCellLabelFontSize = 18
facet_tagsxdmfDisplay.SelectionCellLabelItalic = 0
facet_tagsxdmfDisplay.SelectionCellLabelJustification = 'Left'
facet_tagsxdmfDisplay.SelectionCellLabelOpacity = 1.0
facet_tagsxdmfDisplay.SelectionCellLabelShadow = 0
facet_tagsxdmfDisplay.SelectionPointLabelBold = 0
facet_tagsxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
facet_tagsxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.SelectionPointLabelFontFile = ''
facet_tagsxdmfDisplay.SelectionPointLabelFontSize = 18
facet_tagsxdmfDisplay.SelectionPointLabelItalic = 0
facet_tagsxdmfDisplay.SelectionPointLabelJustification = 'Left'
facet_tagsxdmfDisplay.SelectionPointLabelOpacity = 1.0
facet_tagsxdmfDisplay.SelectionPointLabelShadow = 0
facet_tagsxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
facet_tagsxdmfDisplay.ScalarOpacityFunction = None
facet_tagsxdmfDisplay.ScalarOpacityUnitDistance = 46.58999034360628
facet_tagsxdmfDisplay.UseSeparateOpacityArray = 0
facet_tagsxdmfDisplay.OpacityArrayName = ['CELLS', 'aquifersys_cells']
facet_tagsxdmfDisplay.OpacityComponent = ''
facet_tagsxdmfDisplay.SelectMapper = 'Projected tetra'
facet_tagsxdmfDisplay.SamplingDimensions = [128, 128, 128]
facet_tagsxdmfDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
facet_tagsxdmfDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
facet_tagsxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
facet_tagsxdmfDisplay.GlyphType.TipResolution = 6
facet_tagsxdmfDisplay.GlyphType.TipRadius = 0.1
facet_tagsxdmfDisplay.GlyphType.TipLength = 0.35
facet_tagsxdmfDisplay.GlyphType.ShaftResolution = 6
facet_tagsxdmfDisplay.GlyphType.ShaftRadius = 0.03
facet_tagsxdmfDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
facet_tagsxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
facet_tagsxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
facet_tagsxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
facet_tagsxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
facet_tagsxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
facet_tagsxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
facet_tagsxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
facet_tagsxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.XTitleBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.XTitleItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.XTitleShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.YTitleBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.YTitleItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.YTitleShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.FacesToRender = 63
facet_tagsxdmfDisplay.DataAxesGrid.CullBackface = 0
facet_tagsxdmfDisplay.DataAxesGrid.CullFrontface = 1
facet_tagsxdmfDisplay.DataAxesGrid.ShowGrid = 0
facet_tagsxdmfDisplay.DataAxesGrid.ShowEdges = 1
facet_tagsxdmfDisplay.DataAxesGrid.ShowTicks = 1
facet_tagsxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
facet_tagsxdmfDisplay.DataAxesGrid.AxesToLabel = 63
facet_tagsxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.XLabelBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.XLabelItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.XLabelShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.YLabelBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.YLabelItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.YLabelShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelBold = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
facet_tagsxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
facet_tagsxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
facet_tagsxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
facet_tagsxdmfDisplay.DataAxesGrid.XAxisLabels = []
facet_tagsxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
facet_tagsxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
facet_tagsxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
facet_tagsxdmfDisplay.DataAxesGrid.YAxisLabels = []
facet_tagsxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
facet_tagsxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
facet_tagsxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
facet_tagsxdmfDisplay.DataAxesGrid.ZAxisLabels = []
facet_tagsxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
facet_tagsxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
facet_tagsxdmfDisplay.PolarAxes.Visibility = 0
facet_tagsxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
facet_tagsxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
facet_tagsxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
facet_tagsxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.EnableCustomRange = 0
facet_tagsxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
facet_tagsxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
facet_tagsxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
facet_tagsxdmfDisplay.PolarAxes.AutoSubdividePolarAxis = 1
facet_tagsxdmfDisplay.PolarAxes.NumberOfPolarAxis = 0
facet_tagsxdmfDisplay.PolarAxes.MinimumRadius = 0.0
facet_tagsxdmfDisplay.PolarAxes.MinimumAngle = 0.0
facet_tagsxdmfDisplay.PolarAxes.MaximumAngle = 90.0
facet_tagsxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
facet_tagsxdmfDisplay.PolarAxes.Ratio = 1.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
facet_tagsxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
facet_tagsxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
facet_tagsxdmfDisplay.PolarAxes.RadialLabelVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
facet_tagsxdmfDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
facet_tagsxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.ScreenSize = 10.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
facet_tagsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
facet_tagsxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
facet_tagsxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
facet_tagsxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
facet_tagsxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
facet_tagsxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
facet_tagsxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
facet_tagsxdmfDisplay.PolarAxes.TickLocation = 'Both'
facet_tagsxdmfDisplay.PolarAxes.AxisTickVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
facet_tagsxdmfDisplay.PolarAxes.ArcTickVisibility = 1
facet_tagsxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
facet_tagsxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
facet_tagsxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
facet_tagsxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
facet_tagsxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
facet_tagsxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
facet_tagsxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
facet_tagsxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
facet_tagsxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
facet_tagsxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
facet_tagsxdmfDisplay.PolarAxes.Use2DMode = 0
facet_tagsxdmfDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(facet_tagsxdmfDisplay, ('CELLS', 'aquifersys_cells'))

# rescale color and/or opacity maps used to include current data range
facet_tagsxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
facet_tagsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'aquifersys_cells'
aquifersys_cellsLUT = GetColorTransferFunction('aquifersys_cells')

# get opacity transfer function/opacity map for 'aquifersys_cells'
aquifersys_cellsPWF = GetOpacityTransferFunction('aquifersys_cells')

ImportPresets(filename='layers.json')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aquifersys_cellsLUT.ApplyPreset('layers', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aquifersys_cellsPWF.ApplyPreset('layers', True)

# reset view to fit data
renderView1.ResetCamera(False)

# change representation type
facet_tagsxdmfDisplay.SetRepresentationType('Surface With Edges')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1096, 793)

# current camera placement for renderView1
renderView1.CameraPosition = [8829.697272912243, 1750.0, 150.0]
renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
renderView1.CameraViewUp = [0.0, -4.440892098500626e-16, -1.0]
renderView1.CameraParallelScale = 2026.4747716169575

# save screenshot
SaveScreenshot('../output/plots/mesh_2D_zy.png', renderView1, ImageResolution=[3*1096, 3*793],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5',
    MetaData=['Application', 'ParaView'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1096, 793)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [8829.697272912243, 1750.0, 210.0]
renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
renderView1.CameraViewUp = [0.0, -4.440892098500626e-16, -1.0]
renderView1.CameraParallelScale = 2026.4747716169575

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
