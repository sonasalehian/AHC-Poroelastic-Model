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
ColorBy(facet_tagsxdmfDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
facet_tagsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# set scalar coloring
ColorBy(facet_tagsxdmfDisplay, ('CELLS', 'aquifersys_cells'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
facet_tagsxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
facet_tagsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'aquifersys_cells'
aquifersys_cellsLUT = GetColorTransferFunction('aquifersys_cells')

# get opacity transfer function/opacity map for 'aquifersys_cells'
aquifersys_cellsPWF = GetOpacityTransferFunction('aquifersys_cells')

# reset view to fit data
renderView1.ResetCamera(False)

ImportPresets(filename='./layer.json')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aquifersys_cellsLUT.ApplyPreset('layer', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aquifersys_cellsPWF.ApplyPreset('layer', True)

# create a new 'Line'
line1 = Line(registrationName='Line1')
line1.Point1 = [-0.5, 0.0, 0.0]
line1.Point2 = [0.5, 0.0, 0.0]
line1.UseRegularRefinement = 1
line1.Resolution = 6
line1.RefinementRatios = [0.0, 1.0]

# Properties modified on line1
line1.Point1 = [750.0, 0.0, 0.0]
line1.Point2 = [750.0, 3500.0, 0.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
line1Display = Show(line1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
line1Display.Selection = None
line1Display.Representation = 'Surface'
line1Display.ColorArrayName = [None, '']
line1Display.LookupTable = None
line1Display.MapScalars = 1
line1Display.MultiComponentsMapping = 0
line1Display.InterpolateScalarsBeforeMapping = 1
line1Display.Opacity = 1.0
line1Display.PointSize = 2.0
line1Display.LineWidth = 1.0
line1Display.RenderLinesAsTubes = 0
line1Display.RenderPointsAsSpheres = 0
line1Display.Interpolation = 'Gouraud'
line1Display.Specular = 0.0
line1Display.SpecularColor = [1.0, 1.0, 1.0]
line1Display.SpecularPower = 100.0
line1Display.Luminosity = 0.0
line1Display.Ambient = 0.0
line1Display.Diffuse = 1.0
line1Display.Roughness = 0.3
line1Display.Metallic = 0.0
line1Display.EdgeTint = [1.0, 1.0, 1.0]
line1Display.Anisotropy = 0.0
line1Display.AnisotropyRotation = 0.0
line1Display.BaseIOR = 1.5
line1Display.CoatStrength = 0.0
line1Display.CoatIOR = 2.0
line1Display.CoatRoughness = 0.0
line1Display.CoatColor = [1.0, 1.0, 1.0]
line1Display.SelectTCoordArray = 'Texture Coordinates'
line1Display.SelectNormalArray = 'None'
line1Display.SelectTangentArray = 'None'
line1Display.Texture = None
line1Display.RepeatTextures = 1
line1Display.InterpolateTextures = 0
line1Display.SeamlessU = 0
line1Display.SeamlessV = 0
line1Display.UseMipmapTextures = 0
line1Display.ShowTexturesOnBackface = 1
line1Display.BaseColorTexture = None
line1Display.NormalTexture = None
line1Display.NormalScale = 1.0
line1Display.CoatNormalTexture = None
line1Display.CoatNormalScale = 1.0
line1Display.MaterialTexture = None
line1Display.OcclusionStrength = 1.0
line1Display.AnisotropyTexture = None
line1Display.EmissiveTexture = None
line1Display.EmissiveFactor = [1.0, 1.0, 1.0]
line1Display.FlipTextures = 0
line1Display.BackfaceRepresentation = 'Follow Frontface'
line1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
line1Display.BackfaceOpacity = 1.0
line1Display.Position = [0.0, 0.0, 0.0]
line1Display.Scale = [1.0, 1.0, 1.0]
line1Display.Orientation = [0.0, 0.0, 0.0]
line1Display.Origin = [0.0, 0.0, 0.0]
line1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
line1Display.Pickable = 1
line1Display.Triangulate = 0
line1Display.UseShaderReplacements = 0
line1Display.ShaderReplacements = ''
line1Display.NonlinearSubdivisionLevel = 1
line1Display.UseDataPartitions = 0
line1Display.OSPRayUseScaleArray = 'All Approximate'
line1Display.OSPRayScaleArray = 'Texture Coordinates'
line1Display.OSPRayScaleFunction = 'PiecewiseFunction'
line1Display.OSPRayMaterial = 'None'
line1Display.BlockSelectors = ['/']
line1Display.BlockColors = []
line1Display.BlockOpacities = []
line1Display.Orient = 0
line1Display.OrientationMode = 'Direction'
line1Display.SelectOrientationVectors = 'None'
line1Display.Scaling = 0
line1Display.ScaleMode = 'No Data Scaling Off'
line1Display.ScaleFactor = 350.0
line1Display.SelectScaleArray = 'None'
line1Display.GlyphType = 'Arrow'
line1Display.UseGlyphTable = 0
line1Display.GlyphTableIndexArray = 'None'
line1Display.UseCompositeGlyphTable = 0
line1Display.UseGlyphCullingAndLOD = 0
line1Display.LODValues = []
line1Display.ColorByLODIndex = 0
line1Display.GaussianRadius = 17.5
line1Display.ShaderPreset = 'Sphere'
line1Display.CustomTriangleScale = 3
line1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
line1Display.Emissive = 0
line1Display.ScaleByArray = 0
line1Display.SetScaleArray = ['POINTS', 'Texture Coordinates']
line1Display.ScaleArrayComponent = 'X'
line1Display.UseScaleFunction = 1
line1Display.ScaleTransferFunction = 'PiecewiseFunction'
line1Display.OpacityByArray = 0
line1Display.OpacityArray = ['POINTS', 'Texture Coordinates']
line1Display.OpacityArrayComponent = 'X'
line1Display.OpacityTransferFunction = 'PiecewiseFunction'
line1Display.DataAxesGrid = 'GridAxesRepresentation'
line1Display.SelectionCellLabelBold = 0
line1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
line1Display.SelectionCellLabelFontFamily = 'Arial'
line1Display.SelectionCellLabelFontFile = ''
line1Display.SelectionCellLabelFontSize = 18
line1Display.SelectionCellLabelItalic = 0
line1Display.SelectionCellLabelJustification = 'Left'
line1Display.SelectionCellLabelOpacity = 1.0
line1Display.SelectionCellLabelShadow = 0
line1Display.SelectionPointLabelBold = 0
line1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
line1Display.SelectionPointLabelFontFamily = 'Arial'
line1Display.SelectionPointLabelFontFile = ''
line1Display.SelectionPointLabelFontSize = 18
line1Display.SelectionPointLabelItalic = 0
line1Display.SelectionPointLabelJustification = 'Left'
line1Display.SelectionPointLabelOpacity = 1.0
line1Display.SelectionPointLabelShadow = 0
line1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
line1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
line1Display.GlyphType.TipResolution = 6
line1Display.GlyphType.TipRadius = 0.1
line1Display.GlyphType.TipLength = 0.35
line1Display.GlyphType.ShaftResolution = 6
line1Display.GlyphType.ShaftRadius = 0.03
line1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
line1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
line1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
line1Display.DataAxesGrid.XTitle = 'X Axis'
line1Display.DataAxesGrid.YTitle = 'Y Axis'
line1Display.DataAxesGrid.ZTitle = 'Z Axis'
line1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
line1Display.DataAxesGrid.XTitleFontFile = ''
line1Display.DataAxesGrid.XTitleBold = 0
line1Display.DataAxesGrid.XTitleItalic = 0
line1Display.DataAxesGrid.XTitleFontSize = 12
line1Display.DataAxesGrid.XTitleShadow = 0
line1Display.DataAxesGrid.XTitleOpacity = 1.0
line1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
line1Display.DataAxesGrid.YTitleFontFile = ''
line1Display.DataAxesGrid.YTitleBold = 0
line1Display.DataAxesGrid.YTitleItalic = 0
line1Display.DataAxesGrid.YTitleFontSize = 12
line1Display.DataAxesGrid.YTitleShadow = 0
line1Display.DataAxesGrid.YTitleOpacity = 1.0
line1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
line1Display.DataAxesGrid.ZTitleFontFile = ''
line1Display.DataAxesGrid.ZTitleBold = 0
line1Display.DataAxesGrid.ZTitleItalic = 0
line1Display.DataAxesGrid.ZTitleFontSize = 12
line1Display.DataAxesGrid.ZTitleShadow = 0
line1Display.DataAxesGrid.ZTitleOpacity = 1.0
line1Display.DataAxesGrid.FacesToRender = 63
line1Display.DataAxesGrid.CullBackface = 0
line1Display.DataAxesGrid.CullFrontface = 1
line1Display.DataAxesGrid.ShowGrid = 0
line1Display.DataAxesGrid.ShowEdges = 1
line1Display.DataAxesGrid.ShowTicks = 1
line1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
line1Display.DataAxesGrid.AxesToLabel = 63
line1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
line1Display.DataAxesGrid.XLabelFontFile = ''
line1Display.DataAxesGrid.XLabelBold = 0
line1Display.DataAxesGrid.XLabelItalic = 0
line1Display.DataAxesGrid.XLabelFontSize = 12
line1Display.DataAxesGrid.XLabelShadow = 0
line1Display.DataAxesGrid.XLabelOpacity = 1.0
line1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
line1Display.DataAxesGrid.YLabelFontFile = ''
line1Display.DataAxesGrid.YLabelBold = 0
line1Display.DataAxesGrid.YLabelItalic = 0
line1Display.DataAxesGrid.YLabelFontSize = 12
line1Display.DataAxesGrid.YLabelShadow = 0
line1Display.DataAxesGrid.YLabelOpacity = 1.0
line1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
line1Display.DataAxesGrid.ZLabelFontFile = ''
line1Display.DataAxesGrid.ZLabelBold = 0
line1Display.DataAxesGrid.ZLabelItalic = 0
line1Display.DataAxesGrid.ZLabelFontSize = 12
line1Display.DataAxesGrid.ZLabelShadow = 0
line1Display.DataAxesGrid.ZLabelOpacity = 1.0
line1Display.DataAxesGrid.XAxisNotation = 'Mixed'
line1Display.DataAxesGrid.XAxisPrecision = 2
line1Display.DataAxesGrid.XAxisUseCustomLabels = 0
line1Display.DataAxesGrid.XAxisLabels = []
line1Display.DataAxesGrid.YAxisNotation = 'Mixed'
line1Display.DataAxesGrid.YAxisPrecision = 2
line1Display.DataAxesGrid.YAxisUseCustomLabels = 0
line1Display.DataAxesGrid.YAxisLabels = []
line1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
line1Display.DataAxesGrid.ZAxisPrecision = 2
line1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
line1Display.DataAxesGrid.ZAxisLabels = []
line1Display.DataAxesGrid.UseCustomBounds = 0
line1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
line1Display.PolarAxes.Visibility = 0
line1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
line1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
line1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
line1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
line1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
line1Display.PolarAxes.EnableCustomRange = 0
line1Display.PolarAxes.CustomRange = [0.0, 1.0]
line1Display.PolarAxes.PolarAxisVisibility = 1
line1Display.PolarAxes.RadialAxesVisibility = 1
line1Display.PolarAxes.DrawRadialGridlines = 1
line1Display.PolarAxes.PolarArcsVisibility = 1
line1Display.PolarAxes.DrawPolarArcsGridlines = 1
line1Display.PolarAxes.NumberOfRadialAxes = 0
line1Display.PolarAxes.AutoSubdividePolarAxis = 1
line1Display.PolarAxes.NumberOfPolarAxis = 0
line1Display.PolarAxes.MinimumRadius = 0.0
line1Display.PolarAxes.MinimumAngle = 0.0
line1Display.PolarAxes.MaximumAngle = 90.0
line1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
line1Display.PolarAxes.Ratio = 1.0
line1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
line1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
line1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
line1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
line1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
line1Display.PolarAxes.PolarAxisTitleVisibility = 1
line1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
line1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
line1Display.PolarAxes.PolarLabelVisibility = 1
line1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
line1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
line1Display.PolarAxes.RadialLabelVisibility = 1
line1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
line1Display.PolarAxes.RadialLabelLocation = 'Bottom'
line1Display.PolarAxes.RadialUnitsVisibility = 1
line1Display.PolarAxes.ScreenSize = 10.0
line1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
line1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
line1Display.PolarAxes.PolarAxisTitleFontFile = ''
line1Display.PolarAxes.PolarAxisTitleBold = 0
line1Display.PolarAxes.PolarAxisTitleItalic = 0
line1Display.PolarAxes.PolarAxisTitleShadow = 0
line1Display.PolarAxes.PolarAxisTitleFontSize = 12
line1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
line1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
line1Display.PolarAxes.PolarAxisLabelFontFile = ''
line1Display.PolarAxes.PolarAxisLabelBold = 0
line1Display.PolarAxes.PolarAxisLabelItalic = 0
line1Display.PolarAxes.PolarAxisLabelShadow = 0
line1Display.PolarAxes.PolarAxisLabelFontSize = 12
line1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
line1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
line1Display.PolarAxes.LastRadialAxisTextFontFile = ''
line1Display.PolarAxes.LastRadialAxisTextBold = 0
line1Display.PolarAxes.LastRadialAxisTextItalic = 0
line1Display.PolarAxes.LastRadialAxisTextShadow = 0
line1Display.PolarAxes.LastRadialAxisTextFontSize = 12
line1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
line1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
line1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
line1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
line1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
line1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
line1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
line1Display.PolarAxes.EnableDistanceLOD = 1
line1Display.PolarAxes.DistanceLODThreshold = 0.7
line1Display.PolarAxes.EnableViewAngleLOD = 1
line1Display.PolarAxes.ViewAngleLODThreshold = 0.7
line1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
line1Display.PolarAxes.PolarTicksVisibility = 1
line1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
line1Display.PolarAxes.TickLocation = 'Both'
line1Display.PolarAxes.AxisTickVisibility = 1
line1Display.PolarAxes.AxisMinorTickVisibility = 0
line1Display.PolarAxes.ArcTickVisibility = 1
line1Display.PolarAxes.ArcMinorTickVisibility = 0
line1Display.PolarAxes.DeltaAngleMajor = 10.0
line1Display.PolarAxes.DeltaAngleMinor = 5.0
line1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
line1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
line1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
line1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
line1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
line1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
line1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
line1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
line1Display.PolarAxes.ArcMajorTickSize = 0.0
line1Display.PolarAxes.ArcTickRatioSize = 0.3
line1Display.PolarAxes.ArcMajorTickThickness = 1.0
line1Display.PolarAxes.ArcTickRatioThickness = 0.5
line1Display.PolarAxes.Use2DMode = 0
line1Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(facet_tagsxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=line1)

# get color transfer function/color map for 'u_n'
u_nLUT = GetColorTransferFunction('u_n')

# get opacity transfer function/opacity map for 'u_n'
u_nPWF = GetOpacityTransferFunction('u_n')

# get display properties
facet_tagsxdmfDisplay = GetDisplayProperties(facet_tagsxdmf, view=renderView1)

# create a new 'Line'
line2 = Line(registrationName='Line2')
line2.Point1 = [-0.5, 0.0, 0.0]
line2.Point2 = [0.5, 0.0, 0.0]
line2.UseRegularRefinement = 1
line2.Resolution = 6
line2.RefinementRatios = [0.0, 1.0]

# Properties modified on line2
line2.Point1 = [0.0, 1450.0, 0.0]
line2.Point2 = [2000.0, 1450.0, 0.0]

# show data in view
line2Display = Show(line2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
line2Display.Selection = None
line2Display.Representation = 'Surface'
line2Display.ColorArrayName = [None, '']
line2Display.LookupTable = None
line2Display.MapScalars = 1
line2Display.MultiComponentsMapping = 0
line2Display.InterpolateScalarsBeforeMapping = 1
line2Display.Opacity = 1.0
line2Display.PointSize = 2.0
line2Display.LineWidth = 1.0
line2Display.RenderLinesAsTubes = 0
line2Display.RenderPointsAsSpheres = 0
line2Display.Interpolation = 'Gouraud'
line2Display.Specular = 0.0
line2Display.SpecularColor = [1.0, 1.0, 1.0]
line2Display.SpecularPower = 100.0
line2Display.Luminosity = 0.0
line2Display.Ambient = 0.0
line2Display.Diffuse = 1.0
line2Display.Roughness = 0.3
line2Display.Metallic = 0.0
line2Display.EdgeTint = [1.0, 1.0, 1.0]
line2Display.Anisotropy = 0.0
line2Display.AnisotropyRotation = 0.0
line2Display.BaseIOR = 1.5
line2Display.CoatStrength = 0.0
line2Display.CoatIOR = 2.0
line2Display.CoatRoughness = 0.0
line2Display.CoatColor = [1.0, 1.0, 1.0]
line2Display.SelectTCoordArray = 'Texture Coordinates'
line2Display.SelectNormalArray = 'None'
line2Display.SelectTangentArray = 'None'
line2Display.Texture = None
line2Display.RepeatTextures = 1
line2Display.InterpolateTextures = 0
line2Display.SeamlessU = 0
line2Display.SeamlessV = 0
line2Display.UseMipmapTextures = 0
line2Display.ShowTexturesOnBackface = 1
line2Display.BaseColorTexture = None
line2Display.NormalTexture = None
line2Display.NormalScale = 1.0
line2Display.CoatNormalTexture = None
line2Display.CoatNormalScale = 1.0
line2Display.MaterialTexture = None
line2Display.OcclusionStrength = 1.0
line2Display.AnisotropyTexture = None
line2Display.EmissiveTexture = None
line2Display.EmissiveFactor = [1.0, 1.0, 1.0]
line2Display.FlipTextures = 0
line2Display.BackfaceRepresentation = 'Follow Frontface'
line2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
line2Display.BackfaceOpacity = 1.0
line2Display.Position = [0.0, 0.0, 0.0]
line2Display.Scale = [1.0, 1.0, 1.0]
line2Display.Orientation = [0.0, 0.0, 0.0]
line2Display.Origin = [0.0, 0.0, 0.0]
line2Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
line2Display.Pickable = 1
line2Display.Triangulate = 0
line2Display.UseShaderReplacements = 0
line2Display.ShaderReplacements = ''
line2Display.NonlinearSubdivisionLevel = 1
line2Display.UseDataPartitions = 0
line2Display.OSPRayUseScaleArray = 'All Approximate'
line2Display.OSPRayScaleArray = 'Texture Coordinates'
line2Display.OSPRayScaleFunction = 'PiecewiseFunction'
line2Display.OSPRayMaterial = 'None'
line2Display.BlockSelectors = ['/']
line2Display.BlockColors = []
line2Display.BlockOpacities = []
line2Display.Orient = 0
line2Display.OrientationMode = 'Direction'
line2Display.SelectOrientationVectors = 'None'
line2Display.Scaling = 0
line2Display.ScaleMode = 'No Data Scaling Off'
line2Display.ScaleFactor = 200.0
line2Display.SelectScaleArray = 'None'
line2Display.GlyphType = 'Arrow'
line2Display.UseGlyphTable = 0
line2Display.GlyphTableIndexArray = 'None'
line2Display.UseCompositeGlyphTable = 0
line2Display.UseGlyphCullingAndLOD = 0
line2Display.LODValues = []
line2Display.ColorByLODIndex = 0
line2Display.GaussianRadius = 10.0
line2Display.ShaderPreset = 'Sphere'
line2Display.CustomTriangleScale = 3
line2Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
line2Display.Emissive = 0
line2Display.ScaleByArray = 0
line2Display.SetScaleArray = ['POINTS', 'Texture Coordinates']
line2Display.ScaleArrayComponent = 'X'
line2Display.UseScaleFunction = 1
line2Display.ScaleTransferFunction = 'PiecewiseFunction'
line2Display.OpacityByArray = 0
line2Display.OpacityArray = ['POINTS', 'Texture Coordinates']
line2Display.OpacityArrayComponent = 'X'
line2Display.OpacityTransferFunction = 'PiecewiseFunction'
line2Display.DataAxesGrid = 'GridAxesRepresentation'
line2Display.SelectionCellLabelBold = 0
line2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
line2Display.SelectionCellLabelFontFamily = 'Arial'
line2Display.SelectionCellLabelFontFile = ''
line2Display.SelectionCellLabelFontSize = 18
line2Display.SelectionCellLabelItalic = 0
line2Display.SelectionCellLabelJustification = 'Left'
line2Display.SelectionCellLabelOpacity = 1.0
line2Display.SelectionCellLabelShadow = 0
line2Display.SelectionPointLabelBold = 0
line2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
line2Display.SelectionPointLabelFontFamily = 'Arial'
line2Display.SelectionPointLabelFontFile = ''
line2Display.SelectionPointLabelFontSize = 18
line2Display.SelectionPointLabelItalic = 0
line2Display.SelectionPointLabelJustification = 'Left'
line2Display.SelectionPointLabelOpacity = 1.0
line2Display.SelectionPointLabelShadow = 0
line2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
line2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
line2Display.GlyphType.TipResolution = 6
line2Display.GlyphType.TipRadius = 0.1
line2Display.GlyphType.TipLength = 0.35
line2Display.GlyphType.ShaftResolution = 6
line2Display.GlyphType.ShaftRadius = 0.03
line2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
line2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
line2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
line2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
line2Display.DataAxesGrid.XTitle = 'X Axis'
line2Display.DataAxesGrid.YTitle = 'Y Axis'
line2Display.DataAxesGrid.ZTitle = 'Z Axis'
line2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
line2Display.DataAxesGrid.XTitleFontFile = ''
line2Display.DataAxesGrid.XTitleBold = 0
line2Display.DataAxesGrid.XTitleItalic = 0
line2Display.DataAxesGrid.XTitleFontSize = 12
line2Display.DataAxesGrid.XTitleShadow = 0
line2Display.DataAxesGrid.XTitleOpacity = 1.0
line2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
line2Display.DataAxesGrid.YTitleFontFile = ''
line2Display.DataAxesGrid.YTitleBold = 0
line2Display.DataAxesGrid.YTitleItalic = 0
line2Display.DataAxesGrid.YTitleFontSize = 12
line2Display.DataAxesGrid.YTitleShadow = 0
line2Display.DataAxesGrid.YTitleOpacity = 1.0
line2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
line2Display.DataAxesGrid.ZTitleFontFile = ''
line2Display.DataAxesGrid.ZTitleBold = 0
line2Display.DataAxesGrid.ZTitleItalic = 0
line2Display.DataAxesGrid.ZTitleFontSize = 12
line2Display.DataAxesGrid.ZTitleShadow = 0
line2Display.DataAxesGrid.ZTitleOpacity = 1.0
line2Display.DataAxesGrid.FacesToRender = 63
line2Display.DataAxesGrid.CullBackface = 0
line2Display.DataAxesGrid.CullFrontface = 1
line2Display.DataAxesGrid.ShowGrid = 0
line2Display.DataAxesGrid.ShowEdges = 1
line2Display.DataAxesGrid.ShowTicks = 1
line2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
line2Display.DataAxesGrid.AxesToLabel = 63
line2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
line2Display.DataAxesGrid.XLabelFontFile = ''
line2Display.DataAxesGrid.XLabelBold = 0
line2Display.DataAxesGrid.XLabelItalic = 0
line2Display.DataAxesGrid.XLabelFontSize = 12
line2Display.DataAxesGrid.XLabelShadow = 0
line2Display.DataAxesGrid.XLabelOpacity = 1.0
line2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
line2Display.DataAxesGrid.YLabelFontFile = ''
line2Display.DataAxesGrid.YLabelBold = 0
line2Display.DataAxesGrid.YLabelItalic = 0
line2Display.DataAxesGrid.YLabelFontSize = 12
line2Display.DataAxesGrid.YLabelShadow = 0
line2Display.DataAxesGrid.YLabelOpacity = 1.0
line2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
line2Display.DataAxesGrid.ZLabelFontFile = ''
line2Display.DataAxesGrid.ZLabelBold = 0
line2Display.DataAxesGrid.ZLabelItalic = 0
line2Display.DataAxesGrid.ZLabelFontSize = 12
line2Display.DataAxesGrid.ZLabelShadow = 0
line2Display.DataAxesGrid.ZLabelOpacity = 1.0
line2Display.DataAxesGrid.XAxisNotation = 'Mixed'
line2Display.DataAxesGrid.XAxisPrecision = 2
line2Display.DataAxesGrid.XAxisUseCustomLabels = 0
line2Display.DataAxesGrid.XAxisLabels = []
line2Display.DataAxesGrid.YAxisNotation = 'Mixed'
line2Display.DataAxesGrid.YAxisPrecision = 2
line2Display.DataAxesGrid.YAxisUseCustomLabels = 0
line2Display.DataAxesGrid.YAxisLabels = []
line2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
line2Display.DataAxesGrid.ZAxisPrecision = 2
line2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
line2Display.DataAxesGrid.ZAxisLabels = []
line2Display.DataAxesGrid.UseCustomBounds = 0
line2Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
line2Display.PolarAxes.Visibility = 0
line2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
line2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
line2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
line2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
line2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
line2Display.PolarAxes.EnableCustomRange = 0
line2Display.PolarAxes.CustomRange = [0.0, 1.0]
line2Display.PolarAxes.PolarAxisVisibility = 1
line2Display.PolarAxes.RadialAxesVisibility = 1
line2Display.PolarAxes.DrawRadialGridlines = 1
line2Display.PolarAxes.PolarArcsVisibility = 1
line2Display.PolarAxes.DrawPolarArcsGridlines = 1
line2Display.PolarAxes.NumberOfRadialAxes = 0
line2Display.PolarAxes.AutoSubdividePolarAxis = 1
line2Display.PolarAxes.NumberOfPolarAxis = 0
line2Display.PolarAxes.MinimumRadius = 0.0
line2Display.PolarAxes.MinimumAngle = 0.0
line2Display.PolarAxes.MaximumAngle = 90.0
line2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
line2Display.PolarAxes.Ratio = 1.0
line2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
line2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
line2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
line2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
line2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
line2Display.PolarAxes.PolarAxisTitleVisibility = 1
line2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
line2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
line2Display.PolarAxes.PolarLabelVisibility = 1
line2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
line2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
line2Display.PolarAxes.RadialLabelVisibility = 1
line2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
line2Display.PolarAxes.RadialLabelLocation = 'Bottom'
line2Display.PolarAxes.RadialUnitsVisibility = 1
line2Display.PolarAxes.ScreenSize = 10.0
line2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
line2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
line2Display.PolarAxes.PolarAxisTitleFontFile = ''
line2Display.PolarAxes.PolarAxisTitleBold = 0
line2Display.PolarAxes.PolarAxisTitleItalic = 0
line2Display.PolarAxes.PolarAxisTitleShadow = 0
line2Display.PolarAxes.PolarAxisTitleFontSize = 12
line2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
line2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
line2Display.PolarAxes.PolarAxisLabelFontFile = ''
line2Display.PolarAxes.PolarAxisLabelBold = 0
line2Display.PolarAxes.PolarAxisLabelItalic = 0
line2Display.PolarAxes.PolarAxisLabelShadow = 0
line2Display.PolarAxes.PolarAxisLabelFontSize = 12
line2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
line2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
line2Display.PolarAxes.LastRadialAxisTextFontFile = ''
line2Display.PolarAxes.LastRadialAxisTextBold = 0
line2Display.PolarAxes.LastRadialAxisTextItalic = 0
line2Display.PolarAxes.LastRadialAxisTextShadow = 0
line2Display.PolarAxes.LastRadialAxisTextFontSize = 12
line2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
line2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
line2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
line2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
line2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
line2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
line2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
line2Display.PolarAxes.EnableDistanceLOD = 1
line2Display.PolarAxes.DistanceLODThreshold = 0.7
line2Display.PolarAxes.EnableViewAngleLOD = 1
line2Display.PolarAxes.ViewAngleLODThreshold = 0.7
line2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
line2Display.PolarAxes.PolarTicksVisibility = 1
line2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
line2Display.PolarAxes.TickLocation = 'Both'
line2Display.PolarAxes.AxisTickVisibility = 1
line2Display.PolarAxes.AxisMinorTickVisibility = 0
line2Display.PolarAxes.ArcTickVisibility = 1
line2Display.PolarAxes.ArcMinorTickVisibility = 0
line2Display.PolarAxes.DeltaAngleMajor = 10.0
line2Display.PolarAxes.DeltaAngleMinor = 5.0
line2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
line2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
line2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
line2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
line2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
line2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
line2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
line2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
line2Display.PolarAxes.ArcMajorTickSize = 0.0
line2Display.PolarAxes.ArcTickRatioSize = 0.3
line2Display.PolarAxes.ArcMajorTickThickness = 1.0
line2Display.PolarAxes.ArcTickRatioThickness = 0.5
line2Display.PolarAxes.Use2DMode = 0
line2Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(facet_tagsxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=line2)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1043, 793)

# current camera placement for renderView1
renderView1.CameraPosition = [-3763.6780436308845, -3545.306186832996, -3097.732177060778]
renderView1.CameraFocalPoint = [937.7733958711575, 1419.597887219409, 716.7456748754182]
renderView1.CameraViewUp = [0.3477815865532319, 0.3415146137700418, -0.8731642094337217]
renderView1.CameraParallelScale = 2026.4747716169575

# save screenshot
SaveScreenshot('../output/plots/mesh_3D.png', renderView1, ImageResolution=[3*1043, 3*793],
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
layout1.SetSize(1043, 793)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-3763.6780436308845, -3545.306186832996, -3097.732177060778]
renderView1.CameraFocalPoint = [937.7733958711575, 1419.597887219409, 716.7456748754182]
renderView1.CameraViewUp = [0.3477815865532319, 0.3415146137700418, -0.8731642094337217]
renderView1.CameraParallelScale = 2026.4747716169575

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
