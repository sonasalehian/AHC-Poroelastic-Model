# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os


def plot_LOS_T(inputfile, T):
    
  #### disable automatic camera reset on 'Show'
  paraview.simple._DisableFirstRenderCameraReset()

  # create a new 'ADIOS2VTXReader'
  deformation_LOSbp = ADIOS2VTXReader(registrationName='deformation_LOS.bp', FileName=f'../output/{inputfile}/deformation_LOS.bp')

  # get animation scene
  animationScene1 = GetAnimationScene()

  # update animation scene based on data timesteps
  animationScene1.UpdateAnimationUsingDataTimeSteps()

  # get active view
  renderView1 = GetActiveViewOrCreate('RenderView')

  # show data in view
  deformation_LOSbpDisplay = Show(deformation_LOSbp, renderView1, 'UnstructuredGridRepresentation')

  # trace defaults for the display properties.
  deformation_LOSbpDisplay.Selection = None
  deformation_LOSbpDisplay.Representation = 'Surface'
  deformation_LOSbpDisplay.ColorArrayName = [None, '']
  deformation_LOSbpDisplay.LookupTable = None
  deformation_LOSbpDisplay.MapScalars = 1
  deformation_LOSbpDisplay.MultiComponentsMapping = 0
  deformation_LOSbpDisplay.InterpolateScalarsBeforeMapping = 1
  deformation_LOSbpDisplay.Opacity = 1.0
  deformation_LOSbpDisplay.PointSize = 2.0
  deformation_LOSbpDisplay.LineWidth = 1.0
  deformation_LOSbpDisplay.RenderLinesAsTubes = 0
  deformation_LOSbpDisplay.RenderPointsAsSpheres = 0
  deformation_LOSbpDisplay.Interpolation = 'Gouraud'
  deformation_LOSbpDisplay.Specular = 0.0
  deformation_LOSbpDisplay.SpecularColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.SpecularPower = 100.0
  deformation_LOSbpDisplay.Luminosity = 0.0
  deformation_LOSbpDisplay.Ambient = 0.0
  deformation_LOSbpDisplay.Diffuse = 1.0
  deformation_LOSbpDisplay.Roughness = 0.3
  deformation_LOSbpDisplay.Metallic = 0.0
  deformation_LOSbpDisplay.EdgeTint = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.Anisotropy = 0.0
  deformation_LOSbpDisplay.AnisotropyRotation = 0.0
  deformation_LOSbpDisplay.BaseIOR = 1.5
  deformation_LOSbpDisplay.CoatStrength = 0.0
  deformation_LOSbpDisplay.CoatIOR = 2.0
  deformation_LOSbpDisplay.CoatRoughness = 0.0
  deformation_LOSbpDisplay.CoatColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.SelectTCoordArray = 'None'
  deformation_LOSbpDisplay.SelectNormalArray = 'None'
  deformation_LOSbpDisplay.SelectTangentArray = 'None'
  deformation_LOSbpDisplay.Texture = None
  deformation_LOSbpDisplay.RepeatTextures = 1
  deformation_LOSbpDisplay.InterpolateTextures = 0
  deformation_LOSbpDisplay.SeamlessU = 0
  deformation_LOSbpDisplay.SeamlessV = 0
  deformation_LOSbpDisplay.UseMipmapTextures = 0
  deformation_LOSbpDisplay.ShowTexturesOnBackface = 1
  deformation_LOSbpDisplay.BaseColorTexture = None
  deformation_LOSbpDisplay.NormalTexture = None
  deformation_LOSbpDisplay.NormalScale = 1.0
  deformation_LOSbpDisplay.CoatNormalTexture = None
  deformation_LOSbpDisplay.CoatNormalScale = 1.0
  deformation_LOSbpDisplay.MaterialTexture = None
  deformation_LOSbpDisplay.OcclusionStrength = 1.0
  deformation_LOSbpDisplay.AnisotropyTexture = None
  deformation_LOSbpDisplay.EmissiveTexture = None
  deformation_LOSbpDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.FlipTextures = 0
  deformation_LOSbpDisplay.BackfaceRepresentation = 'Follow Frontface'
  deformation_LOSbpDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.BackfaceOpacity = 1.0
  deformation_LOSbpDisplay.Position = [0.0, 0.0, 0.0]
  deformation_LOSbpDisplay.Scale = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.Orientation = [0.0, 0.0, 0.0]
  deformation_LOSbpDisplay.Origin = [0.0, 0.0, 0.0]
  deformation_LOSbpDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
  deformation_LOSbpDisplay.Pickable = 1
  deformation_LOSbpDisplay.Triangulate = 0
  deformation_LOSbpDisplay.UseShaderReplacements = 0
  deformation_LOSbpDisplay.ShaderReplacements = ''
  deformation_LOSbpDisplay.NonlinearSubdivisionLevel = 1
  deformation_LOSbpDisplay.UseDataPartitions = 0
  deformation_LOSbpDisplay.OSPRayUseScaleArray = 'All Approximate'
  deformation_LOSbpDisplay.OSPRayScaleArray = 'f'
  deformation_LOSbpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
  deformation_LOSbpDisplay.OSPRayMaterial = 'None'
  deformation_LOSbpDisplay.BlockSelectors = ['/']
  deformation_LOSbpDisplay.BlockColors = []
  deformation_LOSbpDisplay.BlockOpacities = []
  deformation_LOSbpDisplay.Orient = 0
  deformation_LOSbpDisplay.OrientationMode = 'Direction'
  deformation_LOSbpDisplay.SelectOrientationVectors = 'None'
  deformation_LOSbpDisplay.Scaling = 0
  deformation_LOSbpDisplay.ScaleMode = 'No Data Scaling Off'
  deformation_LOSbpDisplay.ScaleFactor = 350.00000000000006
  deformation_LOSbpDisplay.SelectScaleArray = 'None'
  deformation_LOSbpDisplay.GlyphType = 'Arrow'
  deformation_LOSbpDisplay.UseGlyphTable = 0
  deformation_LOSbpDisplay.GlyphTableIndexArray = 'None'
  deformation_LOSbpDisplay.UseCompositeGlyphTable = 0
  deformation_LOSbpDisplay.UseGlyphCullingAndLOD = 0
  deformation_LOSbpDisplay.LODValues = []
  deformation_LOSbpDisplay.ColorByLODIndex = 0
  deformation_LOSbpDisplay.GaussianRadius = 17.500000000000004
  deformation_LOSbpDisplay.ShaderPreset = 'Sphere'
  deformation_LOSbpDisplay.CustomTriangleScale = 3
  deformation_LOSbpDisplay.CustomShader = """ // This custom shader code define a gaussian blur
  // Please take a look into vtkSMPointGaussianRepresentation.cxx
  // for other custom shader examples
  //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
  """
  deformation_LOSbpDisplay.Emissive = 0
  deformation_LOSbpDisplay.ScaleByArray = 0
  deformation_LOSbpDisplay.SetScaleArray = ['POINTS', 'f']
  deformation_LOSbpDisplay.ScaleArrayComponent = ''
  deformation_LOSbpDisplay.UseScaleFunction = 1
  deformation_LOSbpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
  deformation_LOSbpDisplay.OpacityByArray = 0
  deformation_LOSbpDisplay.OpacityArray = ['POINTS', 'f']
  deformation_LOSbpDisplay.OpacityArrayComponent = ''
  deformation_LOSbpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
  deformation_LOSbpDisplay.DataAxesGrid = 'GridAxesRepresentation'
  deformation_LOSbpDisplay.SelectionCellLabelBold = 0
  deformation_LOSbpDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
  deformation_LOSbpDisplay.SelectionCellLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.SelectionCellLabelFontFile = ''
  deformation_LOSbpDisplay.SelectionCellLabelFontSize = 18
  deformation_LOSbpDisplay.SelectionCellLabelItalic = 0
  deformation_LOSbpDisplay.SelectionCellLabelJustification = 'Left'
  deformation_LOSbpDisplay.SelectionCellLabelOpacity = 1.0
  deformation_LOSbpDisplay.SelectionCellLabelShadow = 0
  deformation_LOSbpDisplay.SelectionPointLabelBold = 0
  deformation_LOSbpDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
  deformation_LOSbpDisplay.SelectionPointLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.SelectionPointLabelFontFile = ''
  deformation_LOSbpDisplay.SelectionPointLabelFontSize = 18
  deformation_LOSbpDisplay.SelectionPointLabelItalic = 0
  deformation_LOSbpDisplay.SelectionPointLabelJustification = 'Left'
  deformation_LOSbpDisplay.SelectionPointLabelOpacity = 1.0
  deformation_LOSbpDisplay.SelectionPointLabelShadow = 0
  deformation_LOSbpDisplay.PolarAxes = 'PolarAxesRepresentation'
  deformation_LOSbpDisplay.ScalarOpacityFunction = None
  deformation_LOSbpDisplay.ScalarOpacityUnitDistance = 59.8130778687876
  deformation_LOSbpDisplay.UseSeparateOpacityArray = 0
  deformation_LOSbpDisplay.OpacityArrayName = ['POINTS', 'f']
  deformation_LOSbpDisplay.OpacityComponent = ''
  deformation_LOSbpDisplay.SelectMapper = 'Projected tetra'
  deformation_LOSbpDisplay.SamplingDimensions = [128, 128, 128]
  deformation_LOSbpDisplay.UseFloatingPointFrameBuffer = 1

  # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
  deformation_LOSbpDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
  deformation_LOSbpDisplay.OSPRayScaleFunction.UseLogScale = 0

  # init the 'Arrow' selected for 'GlyphType'
  deformation_LOSbpDisplay.GlyphType.TipResolution = 6
  deformation_LOSbpDisplay.GlyphType.TipRadius = 0.1
  deformation_LOSbpDisplay.GlyphType.TipLength = 0.35
  deformation_LOSbpDisplay.GlyphType.ShaftResolution = 6
  deformation_LOSbpDisplay.GlyphType.ShaftRadius = 0.03
  deformation_LOSbpDisplay.GlyphType.Invert = 0

  # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
  deformation_LOSbpDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  deformation_LOSbpDisplay.ScaleTransferFunction.UseLogScale = 0

  # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
  deformation_LOSbpDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  deformation_LOSbpDisplay.OpacityTransferFunction.UseLogScale = 0

  # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
  deformation_LOSbpDisplay.DataAxesGrid.XTitle = 'X Axis'
  deformation_LOSbpDisplay.DataAxesGrid.YTitle = 'Y Axis'
  deformation_LOSbpDisplay.DataAxesGrid.ZTitle = 'Z Axis'
  deformation_LOSbpDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.XTitleFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.XTitleBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.XTitleItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.XTitleFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.XTitleShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.XTitleOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.YTitleFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.YTitleBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.YTitleItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.YTitleFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.YTitleShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.YTitleOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZTitleOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.FacesToRender = 63
  deformation_LOSbpDisplay.DataAxesGrid.CullBackface = 0
  deformation_LOSbpDisplay.DataAxesGrid.CullFrontface = 1
  deformation_LOSbpDisplay.DataAxesGrid.ShowGrid = 0
  deformation_LOSbpDisplay.DataAxesGrid.ShowEdges = 1
  deformation_LOSbpDisplay.DataAxesGrid.ShowTicks = 1
  deformation_LOSbpDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
  deformation_LOSbpDisplay.DataAxesGrid.AxesToLabel = 63
  deformation_LOSbpDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.XLabelFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.XLabelBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.XLabelItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.XLabelFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.XLabelShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.XLabelOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.YLabelFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.YLabelBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.YLabelItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.YLabelFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.YLabelShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.YLabelOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontFile = ''
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelBold = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelItalic = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontSize = 12
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelShadow = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZLabelOpacity = 1.0
  deformation_LOSbpDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
  deformation_LOSbpDisplay.DataAxesGrid.XAxisPrecision = 2
  deformation_LOSbpDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
  deformation_LOSbpDisplay.DataAxesGrid.XAxisLabels = []
  deformation_LOSbpDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
  deformation_LOSbpDisplay.DataAxesGrid.YAxisPrecision = 2
  deformation_LOSbpDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
  deformation_LOSbpDisplay.DataAxesGrid.YAxisLabels = []
  deformation_LOSbpDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
  deformation_LOSbpDisplay.DataAxesGrid.ZAxisPrecision = 2
  deformation_LOSbpDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
  deformation_LOSbpDisplay.DataAxesGrid.ZAxisLabels = []
  deformation_LOSbpDisplay.DataAxesGrid.UseCustomBounds = 0
  deformation_LOSbpDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

  # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
  deformation_LOSbpDisplay.PolarAxes.Visibility = 0
  deformation_LOSbpDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
  deformation_LOSbpDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
  deformation_LOSbpDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
  deformation_LOSbpDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.EnableCustomRange = 0
  deformation_LOSbpDisplay.PolarAxes.CustomRange = [0.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.PolarAxisVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.RadialAxesVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.DrawRadialGridlines = 1
  deformation_LOSbpDisplay.PolarAxes.PolarArcsVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.DrawPolarArcsGridlines = 1
  deformation_LOSbpDisplay.PolarAxes.NumberOfRadialAxes = 0
  deformation_LOSbpDisplay.PolarAxes.AutoSubdividePolarAxis = 1
  deformation_LOSbpDisplay.PolarAxes.NumberOfPolarAxis = 0
  deformation_LOSbpDisplay.PolarAxes.MinimumRadius = 0.0
  deformation_LOSbpDisplay.PolarAxes.MinimumAngle = 0.0
  deformation_LOSbpDisplay.PolarAxes.MaximumAngle = 90.0
  deformation_LOSbpDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
  deformation_LOSbpDisplay.PolarAxes.Ratio = 1.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
  deformation_LOSbpDisplay.PolarAxes.PolarLabelVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
  deformation_LOSbpDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
  deformation_LOSbpDisplay.PolarAxes.RadialLabelVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
  deformation_LOSbpDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
  deformation_LOSbpDisplay.PolarAxes.RadialUnitsVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.ScreenSize = 10.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontFile = ''
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleBold = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleItalic = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleShadow = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontSize = 12
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontFile = ''
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelBold = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelItalic = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelShadow = 0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontSize = 12
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextBold = 0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextItalic = 0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextShadow = 0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
  deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
  deformation_LOSbpDisplay.PolarAxes.EnableDistanceLOD = 1
  deformation_LOSbpDisplay.PolarAxes.DistanceLODThreshold = 0.7
  deformation_LOSbpDisplay.PolarAxes.EnableViewAngleLOD = 1
  deformation_LOSbpDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
  deformation_LOSbpDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
  deformation_LOSbpDisplay.PolarAxes.PolarTicksVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
  deformation_LOSbpDisplay.PolarAxes.TickLocation = 'Both'
  deformation_LOSbpDisplay.PolarAxes.AxisTickVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.AxisMinorTickVisibility = 0
  deformation_LOSbpDisplay.PolarAxes.ArcTickVisibility = 1
  deformation_LOSbpDisplay.PolarAxes.ArcMinorTickVisibility = 0
  deformation_LOSbpDisplay.PolarAxes.DeltaAngleMajor = 10.0
  deformation_LOSbpDisplay.PolarAxes.DeltaAngleMinor = 5.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
  deformation_LOSbpDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
  deformation_LOSbpDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
  deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
  deformation_LOSbpDisplay.PolarAxes.ArcMajorTickSize = 0.0
  deformation_LOSbpDisplay.PolarAxes.ArcTickRatioSize = 0.3
  deformation_LOSbpDisplay.PolarAxes.ArcMajorTickThickness = 1.0
  deformation_LOSbpDisplay.PolarAxes.ArcTickRatioThickness = 0.5
  deformation_LOSbpDisplay.PolarAxes.Use2DMode = 0
  deformation_LOSbpDisplay.PolarAxes.UseLogAxis = 0

  # reset view to fit data
  renderView1.ResetCamera(False)

  # get the material library
  materialLibrary1 = GetMaterialLibrary()

  # update the view to ensure updated data information
  renderView1.Update()

  # set scalar coloring
  ColorBy(deformation_LOSbpDisplay, ('POINTS', 'f'))

  # rescale color and/or opacity maps used to include current data range
  deformation_LOSbpDisplay.RescaleTransferFunctionToDataRange(True, False)

  # show color bar/color legend
  deformation_LOSbpDisplay.SetScalarBarVisibility(renderView1, True)

  # get color transfer function/color map for 'f'
  fLUT = GetColorTransferFunction('f')

  # get opacity transfer function/opacity map for 'f'
  fPWF = GetOpacityTransferFunction('f')

  # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
  fLUT.ApplyPreset('Viridis (matplotlib)', True)

  # invert the transfer function
  fLUT.InvertTransferFunction()

  # Properties modified on animationScene1
  animationScene1.AnimationTime = T

  # get the time-keeper
  timeKeeper1 = GetTimeKeeper()

  # reset view to fit data
  renderView1.ResetCamera(False)

  # Rescale transfer function
  fLUT.RescaleTransferFunction(-0.018, 0.0006)

  # Rescale transfer function
  fPWF.RescaleTransferFunction(-0.018, 0.0006)

  # # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
  # fLUT.ApplyPreset('Viridis (matplotlib)', True)

  # get layout
  layout1 = GetLayout()

  # layout/tab size in pixels
  layout1.SetSize(1096, 793)

  # current camera placement for renderView1
  renderView1.CameraPosition = [1000.0, 1750.0, -7619.697272912243]
  renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
  renderView1.CameraViewUp = [0.5877852522924731, 0.8090169943749475, 0.0]
  renderView1.CameraParallelScale = 2026.4747716169575

  # Make the flux directory
  directory = "strong_long_pumping"
    
  # Parent Directory path
  parent_dir = "../output/plots"
    
  # Path
  path = os.path.join(parent_dir, directory)
  # Check whether the specified path exists or not
  isExist = os.path.exists(path)
  if not isExist:
    # Create the directory
    os.mkdir(path)

  # save screenshot
  SaveScreenshot(f'../output/plots/strong_long_pumping/{inputfile}_LOS_t=T.png', renderView1, ImageResolution=[3*1096, 3*793],
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
  renderView1.CameraPosition = [1000.0, 1750.0, -7619.697272912243]
  renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
  renderView1.CameraViewUp = [0.5877852522924731, 0.8090169943749475, 0.0]
  renderView1.CameraParallelScale = 2026.4747716169575

  #--------------------------------------------
  # uncomment the following to render all views
  # RenderAllViews()
  # alternatively, if you want to write images, you can use SaveScreenshot(...).

def data_LOS_T(inputfile, T):
  directions = ['x', 'y']
  for direction in directions:
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'ADIOS2VTXReader'
    deformation_LOSbp = ADIOS2VTXReader(registrationName='deformation_LOS.bp', FileName=f'../output/{inputfile}/deformation_LOS.bp')

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    deformation_LOSbpDisplay = Show(deformation_LOSbp, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    deformation_LOSbpDisplay.Selection = None
    deformation_LOSbpDisplay.Representation = 'Surface'
    deformation_LOSbpDisplay.ColorArrayName = [None, '']
    deformation_LOSbpDisplay.LookupTable = None
    deformation_LOSbpDisplay.MapScalars = 1
    deformation_LOSbpDisplay.MultiComponentsMapping = 0
    deformation_LOSbpDisplay.InterpolateScalarsBeforeMapping = 1
    deformation_LOSbpDisplay.Opacity = 1.0
    deformation_LOSbpDisplay.PointSize = 2.0
    deformation_LOSbpDisplay.LineWidth = 1.0
    deformation_LOSbpDisplay.RenderLinesAsTubes = 0
    deformation_LOSbpDisplay.RenderPointsAsSpheres = 0
    deformation_LOSbpDisplay.Interpolation = 'Gouraud'
    deformation_LOSbpDisplay.Specular = 0.0
    deformation_LOSbpDisplay.SpecularColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.SpecularPower = 100.0
    deformation_LOSbpDisplay.Luminosity = 0.0
    deformation_LOSbpDisplay.Ambient = 0.0
    deformation_LOSbpDisplay.Diffuse = 1.0
    deformation_LOSbpDisplay.Roughness = 0.3
    deformation_LOSbpDisplay.Metallic = 0.0
    deformation_LOSbpDisplay.EdgeTint = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.Anisotropy = 0.0
    deformation_LOSbpDisplay.AnisotropyRotation = 0.0
    deformation_LOSbpDisplay.BaseIOR = 1.5
    deformation_LOSbpDisplay.CoatStrength = 0.0
    deformation_LOSbpDisplay.CoatIOR = 2.0
    deformation_LOSbpDisplay.CoatRoughness = 0.0
    deformation_LOSbpDisplay.CoatColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.SelectTCoordArray = 'None'
    deformation_LOSbpDisplay.SelectNormalArray = 'None'
    deformation_LOSbpDisplay.SelectTangentArray = 'None'
    deformation_LOSbpDisplay.Texture = None
    deformation_LOSbpDisplay.RepeatTextures = 1
    deformation_LOSbpDisplay.InterpolateTextures = 0
    deformation_LOSbpDisplay.SeamlessU = 0
    deformation_LOSbpDisplay.SeamlessV = 0
    deformation_LOSbpDisplay.UseMipmapTextures = 0
    deformation_LOSbpDisplay.ShowTexturesOnBackface = 1
    deformation_LOSbpDisplay.BaseColorTexture = None
    deformation_LOSbpDisplay.NormalTexture = None
    deformation_LOSbpDisplay.NormalScale = 1.0
    deformation_LOSbpDisplay.CoatNormalTexture = None
    deformation_LOSbpDisplay.CoatNormalScale = 1.0
    deformation_LOSbpDisplay.MaterialTexture = None
    deformation_LOSbpDisplay.OcclusionStrength = 1.0
    deformation_LOSbpDisplay.AnisotropyTexture = None
    deformation_LOSbpDisplay.EmissiveTexture = None
    deformation_LOSbpDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.FlipTextures = 0
    deformation_LOSbpDisplay.BackfaceRepresentation = 'Follow Frontface'
    deformation_LOSbpDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.BackfaceOpacity = 1.0
    deformation_LOSbpDisplay.Position = [0.0, 0.0, 0.0]
    deformation_LOSbpDisplay.Scale = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.Orientation = [0.0, 0.0, 0.0]
    deformation_LOSbpDisplay.Origin = [0.0, 0.0, 0.0]
    deformation_LOSbpDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    deformation_LOSbpDisplay.Pickable = 1
    deformation_LOSbpDisplay.Triangulate = 0
    deformation_LOSbpDisplay.UseShaderReplacements = 0
    deformation_LOSbpDisplay.ShaderReplacements = ''
    deformation_LOSbpDisplay.NonlinearSubdivisionLevel = 1
    deformation_LOSbpDisplay.UseDataPartitions = 0
    deformation_LOSbpDisplay.OSPRayUseScaleArray = 'All Approximate'
    deformation_LOSbpDisplay.OSPRayScaleArray = 'f'
    deformation_LOSbpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    deformation_LOSbpDisplay.OSPRayMaterial = 'None'
    deformation_LOSbpDisplay.BlockSelectors = ['/']
    deformation_LOSbpDisplay.BlockColors = []
    deformation_LOSbpDisplay.BlockOpacities = []
    deformation_LOSbpDisplay.Orient = 0
    deformation_LOSbpDisplay.OrientationMode = 'Direction'
    deformation_LOSbpDisplay.SelectOrientationVectors = 'None'
    deformation_LOSbpDisplay.Scaling = 0
    deformation_LOSbpDisplay.ScaleMode = 'No Data Scaling Off'
    deformation_LOSbpDisplay.ScaleFactor = 350.00000000000006
    deformation_LOSbpDisplay.SelectScaleArray = 'None'
    deformation_LOSbpDisplay.GlyphType = 'Arrow'
    deformation_LOSbpDisplay.UseGlyphTable = 0
    deformation_LOSbpDisplay.GlyphTableIndexArray = 'None'
    deformation_LOSbpDisplay.UseCompositeGlyphTable = 0
    deformation_LOSbpDisplay.UseGlyphCullingAndLOD = 0
    deformation_LOSbpDisplay.LODValues = []
    deformation_LOSbpDisplay.ColorByLODIndex = 0
    deformation_LOSbpDisplay.GaussianRadius = 17.500000000000004
    deformation_LOSbpDisplay.ShaderPreset = 'Sphere'
    deformation_LOSbpDisplay.CustomTriangleScale = 3
    deformation_LOSbpDisplay.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    deformation_LOSbpDisplay.Emissive = 0
    deformation_LOSbpDisplay.ScaleByArray = 0
    deformation_LOSbpDisplay.SetScaleArray = ['POINTS', 'f']
    deformation_LOSbpDisplay.ScaleArrayComponent = ''
    deformation_LOSbpDisplay.UseScaleFunction = 1
    deformation_LOSbpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    deformation_LOSbpDisplay.OpacityByArray = 0
    deformation_LOSbpDisplay.OpacityArray = ['POINTS', 'f']
    deformation_LOSbpDisplay.OpacityArrayComponent = ''
    deformation_LOSbpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    deformation_LOSbpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    deformation_LOSbpDisplay.SelectionCellLabelBold = 0
    deformation_LOSbpDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    deformation_LOSbpDisplay.SelectionCellLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.SelectionCellLabelFontFile = ''
    deformation_LOSbpDisplay.SelectionCellLabelFontSize = 18
    deformation_LOSbpDisplay.SelectionCellLabelItalic = 0
    deformation_LOSbpDisplay.SelectionCellLabelJustification = 'Left'
    deformation_LOSbpDisplay.SelectionCellLabelOpacity = 1.0
    deformation_LOSbpDisplay.SelectionCellLabelShadow = 0
    deformation_LOSbpDisplay.SelectionPointLabelBold = 0
    deformation_LOSbpDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    deformation_LOSbpDisplay.SelectionPointLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.SelectionPointLabelFontFile = ''
    deformation_LOSbpDisplay.SelectionPointLabelFontSize = 18
    deformation_LOSbpDisplay.SelectionPointLabelItalic = 0
    deformation_LOSbpDisplay.SelectionPointLabelJustification = 'Left'
    deformation_LOSbpDisplay.SelectionPointLabelOpacity = 1.0
    deformation_LOSbpDisplay.SelectionPointLabelShadow = 0
    deformation_LOSbpDisplay.PolarAxes = 'PolarAxesRepresentation'
    deformation_LOSbpDisplay.ScalarOpacityFunction = None
    deformation_LOSbpDisplay.ScalarOpacityUnitDistance = 59.8130778687876
    deformation_LOSbpDisplay.UseSeparateOpacityArray = 0
    deformation_LOSbpDisplay.OpacityArrayName = ['POINTS', 'f']
    deformation_LOSbpDisplay.OpacityComponent = ''
    deformation_LOSbpDisplay.SelectMapper = 'Projected tetra'
    deformation_LOSbpDisplay.SamplingDimensions = [128, 128, 128]
    deformation_LOSbpDisplay.UseFloatingPointFrameBuffer = 1

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    deformation_LOSbpDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    deformation_LOSbpDisplay.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    deformation_LOSbpDisplay.GlyphType.TipResolution = 6
    deformation_LOSbpDisplay.GlyphType.TipRadius = 0.1
    deformation_LOSbpDisplay.GlyphType.TipLength = 0.35
    deformation_LOSbpDisplay.GlyphType.ShaftResolution = 6
    deformation_LOSbpDisplay.GlyphType.ShaftRadius = 0.03
    deformation_LOSbpDisplay.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    deformation_LOSbpDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    deformation_LOSbpDisplay.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    deformation_LOSbpDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    deformation_LOSbpDisplay.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    deformation_LOSbpDisplay.DataAxesGrid.XTitle = 'X Axis'
    deformation_LOSbpDisplay.DataAxesGrid.YTitle = 'Y Axis'
    deformation_LOSbpDisplay.DataAxesGrid.ZTitle = 'Z Axis'
    deformation_LOSbpDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.XTitleFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.XTitleBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.XTitleItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.XTitleFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.XTitleShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.XTitleOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.YTitleFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.YTitleBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.YTitleItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.YTitleFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.YTitleShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.YTitleOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZTitleOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.FacesToRender = 63
    deformation_LOSbpDisplay.DataAxesGrid.CullBackface = 0
    deformation_LOSbpDisplay.DataAxesGrid.CullFrontface = 1
    deformation_LOSbpDisplay.DataAxesGrid.ShowGrid = 0
    deformation_LOSbpDisplay.DataAxesGrid.ShowEdges = 1
    deformation_LOSbpDisplay.DataAxesGrid.ShowTicks = 1
    deformation_LOSbpDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
    deformation_LOSbpDisplay.DataAxesGrid.AxesToLabel = 63
    deformation_LOSbpDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.XLabelFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.XLabelBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.XLabelItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.XLabelFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.XLabelShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.XLabelOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.YLabelFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.YLabelBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.YLabelItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.YLabelFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.YLabelShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.YLabelOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontFile = ''
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelBold = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelItalic = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelFontSize = 12
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelShadow = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZLabelOpacity = 1.0
    deformation_LOSbpDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
    deformation_LOSbpDisplay.DataAxesGrid.XAxisPrecision = 2
    deformation_LOSbpDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
    deformation_LOSbpDisplay.DataAxesGrid.XAxisLabels = []
    deformation_LOSbpDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
    deformation_LOSbpDisplay.DataAxesGrid.YAxisPrecision = 2
    deformation_LOSbpDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
    deformation_LOSbpDisplay.DataAxesGrid.YAxisLabels = []
    deformation_LOSbpDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
    deformation_LOSbpDisplay.DataAxesGrid.ZAxisPrecision = 2
    deformation_LOSbpDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
    deformation_LOSbpDisplay.DataAxesGrid.ZAxisLabels = []
    deformation_LOSbpDisplay.DataAxesGrid.UseCustomBounds = 0
    deformation_LOSbpDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    deformation_LOSbpDisplay.PolarAxes.Visibility = 0
    deformation_LOSbpDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
    deformation_LOSbpDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    deformation_LOSbpDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
    deformation_LOSbpDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.EnableCustomRange = 0
    deformation_LOSbpDisplay.PolarAxes.CustomRange = [0.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.PolarAxisVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.RadialAxesVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.DrawRadialGridlines = 1
    deformation_LOSbpDisplay.PolarAxes.PolarArcsVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.DrawPolarArcsGridlines = 1
    deformation_LOSbpDisplay.PolarAxes.NumberOfRadialAxes = 0
    deformation_LOSbpDisplay.PolarAxes.AutoSubdividePolarAxis = 1
    deformation_LOSbpDisplay.PolarAxes.NumberOfPolarAxis = 0
    deformation_LOSbpDisplay.PolarAxes.MinimumRadius = 0.0
    deformation_LOSbpDisplay.PolarAxes.MinimumAngle = 0.0
    deformation_LOSbpDisplay.PolarAxes.MaximumAngle = 90.0
    deformation_LOSbpDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
    deformation_LOSbpDisplay.PolarAxes.Ratio = 1.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    deformation_LOSbpDisplay.PolarAxes.PolarLabelVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
    deformation_LOSbpDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
    deformation_LOSbpDisplay.PolarAxes.RadialLabelVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
    deformation_LOSbpDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
    deformation_LOSbpDisplay.PolarAxes.RadialUnitsVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.ScreenSize = 10.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontFile = ''
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleBold = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleItalic = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleShadow = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTitleFontSize = 12
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontFile = ''
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelBold = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelItalic = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelShadow = 0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisLabelFontSize = 12
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextBold = 0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextItalic = 0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextShadow = 0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
    deformation_LOSbpDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    deformation_LOSbpDisplay.PolarAxes.EnableDistanceLOD = 1
    deformation_LOSbpDisplay.PolarAxes.DistanceLODThreshold = 0.7
    deformation_LOSbpDisplay.PolarAxes.EnableViewAngleLOD = 1
    deformation_LOSbpDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
    deformation_LOSbpDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
    deformation_LOSbpDisplay.PolarAxes.PolarTicksVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
    deformation_LOSbpDisplay.PolarAxes.TickLocation = 'Both'
    deformation_LOSbpDisplay.PolarAxes.AxisTickVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.AxisMinorTickVisibility = 0
    deformation_LOSbpDisplay.PolarAxes.ArcTickVisibility = 1
    deformation_LOSbpDisplay.PolarAxes.ArcMinorTickVisibility = 0
    deformation_LOSbpDisplay.PolarAxes.DeltaAngleMajor = 10.0
    deformation_LOSbpDisplay.PolarAxes.DeltaAngleMinor = 5.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
    deformation_LOSbpDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
    deformation_LOSbpDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    deformation_LOSbpDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    deformation_LOSbpDisplay.PolarAxes.ArcMajorTickSize = 0.0
    deformation_LOSbpDisplay.PolarAxes.ArcTickRatioSize = 0.3
    deformation_LOSbpDisplay.PolarAxes.ArcMajorTickThickness = 1.0
    deformation_LOSbpDisplay.PolarAxes.ArcTickRatioThickness = 0.5
    deformation_LOSbpDisplay.PolarAxes.Use2DMode = 0
    deformation_LOSbpDisplay.PolarAxes.UseLogAxis = 0

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(deformation_LOSbpDisplay, ('POINTS', 'f'))

    # rescale color and/or opacity maps used to include current data range
    deformation_LOSbpDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    deformation_LOSbpDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'f'
    fLUT = GetColorTransferFunction('f')

    # get opacity transfer function/opacity map for 'f'
    fPWF = GetOpacityTransferFunction('f')

    # Properties modified on animationScene1
    animationScene1.AnimationTime = T

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    # create a new 'Plot Over Line'
    plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=deformation_LOSbp)
    plotOverLine1.Point1 = [0.0, 0.0, 0.0]
    plotOverLine1.Point2 = [2000.0000000000002, 3500.0000000000005, 300.00000000000006]
    plotOverLine1.SamplingPattern = 'Sample Uniformly'
    plotOverLine1.Resolution = 1000
    plotOverLine1.PassPartialArrays = 1
    plotOverLine1.PassCellArrays = 0
    plotOverLine1.PassPointArrays = 0
    plotOverLine1.PassFieldArrays = 1
    plotOverLine1.ComputeTolerance = 1
    plotOverLine1.Tolerance = 2.220446049250313e-16

    # Properties modified on plotOverLine1
    if direction == 'x':
      plotOverLine1.Point1 = [750.0, 0.0, 0.0]
      plotOverLine1.Point2 = [750.0, 3500.0000000000005, 0.0]
    elif direction =='y':
      plotOverLine1.Point1 = [0.0, 1450.0, 0.0]
      plotOverLine1.Point2 = [2000.0000000000002, 1450.0, 0.0]

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'f'
    fLUT = GetColorTransferFunction('f')

    # trace defaults for the display properties.
    plotOverLine1Display.Selection = None
    plotOverLine1Display.Representation = 'Surface'
    plotOverLine1Display.ColorArrayName = ['POINTS', 'f']
    plotOverLine1Display.LookupTable = fLUT
    plotOverLine1Display.MapScalars = 1
    plotOverLine1Display.MultiComponentsMapping = 0
    plotOverLine1Display.InterpolateScalarsBeforeMapping = 1
    plotOverLine1Display.Opacity = 1.0
    plotOverLine1Display.PointSize = 2.0
    plotOverLine1Display.LineWidth = 1.0
    plotOverLine1Display.RenderLinesAsTubes = 0
    plotOverLine1Display.RenderPointsAsSpheres = 0
    plotOverLine1Display.Interpolation = 'Gouraud'
    plotOverLine1Display.Specular = 0.0
    plotOverLine1Display.SpecularColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.SpecularPower = 100.0
    plotOverLine1Display.Luminosity = 0.0
    plotOverLine1Display.Ambient = 0.0
    plotOverLine1Display.Diffuse = 1.0
    plotOverLine1Display.Roughness = 0.3
    plotOverLine1Display.Metallic = 0.0
    plotOverLine1Display.EdgeTint = [1.0, 1.0, 1.0]
    plotOverLine1Display.Anisotropy = 0.0
    plotOverLine1Display.AnisotropyRotation = 0.0
    plotOverLine1Display.BaseIOR = 1.5
    plotOverLine1Display.CoatStrength = 0.0
    plotOverLine1Display.CoatIOR = 2.0
    plotOverLine1Display.CoatRoughness = 0.0
    plotOverLine1Display.CoatColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.SelectTCoordArray = 'None'
    plotOverLine1Display.SelectNormalArray = 'None'
    plotOverLine1Display.SelectTangentArray = 'None'
    plotOverLine1Display.Texture = None
    plotOverLine1Display.RepeatTextures = 1
    plotOverLine1Display.InterpolateTextures = 0
    plotOverLine1Display.SeamlessU = 0
    plotOverLine1Display.SeamlessV = 0
    plotOverLine1Display.UseMipmapTextures = 0
    plotOverLine1Display.ShowTexturesOnBackface = 1
    plotOverLine1Display.BaseColorTexture = None
    plotOverLine1Display.NormalTexture = None
    plotOverLine1Display.NormalScale = 1.0
    plotOverLine1Display.CoatNormalTexture = None
    plotOverLine1Display.CoatNormalScale = 1.0
    plotOverLine1Display.MaterialTexture = None
    plotOverLine1Display.OcclusionStrength = 1.0
    plotOverLine1Display.AnisotropyTexture = None
    plotOverLine1Display.EmissiveTexture = None
    plotOverLine1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    plotOverLine1Display.FlipTextures = 0
    plotOverLine1Display.BackfaceRepresentation = 'Follow Frontface'
    plotOverLine1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.BackfaceOpacity = 1.0
    plotOverLine1Display.Position = [0.0, 0.0, 0.0]
    plotOverLine1Display.Scale = [1.0, 1.0, 1.0]
    plotOverLine1Display.Orientation = [0.0, 0.0, 0.0]
    plotOverLine1Display.Origin = [0.0, 0.0, 0.0]
    plotOverLine1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    plotOverLine1Display.Pickable = 1
    plotOverLine1Display.Triangulate = 0
    plotOverLine1Display.UseShaderReplacements = 0
    plotOverLine1Display.ShaderReplacements = ''
    plotOverLine1Display.NonlinearSubdivisionLevel = 1
    plotOverLine1Display.UseDataPartitions = 0
    plotOverLine1Display.OSPRayUseScaleArray = 'All Approximate'
    plotOverLine1Display.OSPRayScaleArray = 'arc_length'
    plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    plotOverLine1Display.OSPRayMaterial = 'None'
    plotOverLine1Display.BlockSelectors = ['/']
    plotOverLine1Display.BlockColors = []
    plotOverLine1Display.BlockOpacities = []
    plotOverLine1Display.Orient = 0
    plotOverLine1Display.OrientationMode = 'Direction'
    plotOverLine1Display.SelectOrientationVectors = 'None'
    plotOverLine1Display.Scaling = 0
    plotOverLine1Display.ScaleMode = 'No Data Scaling Off'
    plotOverLine1Display.ScaleFactor = 350.0
    plotOverLine1Display.SelectScaleArray = 'None'
    plotOverLine1Display.GlyphType = 'Arrow'
    plotOverLine1Display.UseGlyphTable = 0
    plotOverLine1Display.GlyphTableIndexArray = 'None'
    plotOverLine1Display.UseCompositeGlyphTable = 0
    plotOverLine1Display.UseGlyphCullingAndLOD = 0
    plotOverLine1Display.LODValues = []
    plotOverLine1Display.ColorByLODIndex = 0
    plotOverLine1Display.GaussianRadius = 17.5
    plotOverLine1Display.ShaderPreset = 'Sphere'
    plotOverLine1Display.CustomTriangleScale = 3
    plotOverLine1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    plotOverLine1Display.Emissive = 0
    plotOverLine1Display.ScaleByArray = 0
    plotOverLine1Display.SetScaleArray = ['POINTS', 'arc_length']
    plotOverLine1Display.ScaleArrayComponent = ''
    plotOverLine1Display.UseScaleFunction = 1
    plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.OpacityByArray = 0
    plotOverLine1Display.OpacityArray = ['POINTS', 'arc_length']
    plotOverLine1Display.OpacityArrayComponent = ''
    plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
    plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
    plotOverLine1Display.SelectionCellLabelBold = 0
    plotOverLine1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    plotOverLine1Display.SelectionCellLabelFontFamily = 'Arial'
    plotOverLine1Display.SelectionCellLabelFontFile = ''
    plotOverLine1Display.SelectionCellLabelFontSize = 18
    plotOverLine1Display.SelectionCellLabelItalic = 0
    plotOverLine1Display.SelectionCellLabelJustification = 'Left'
    plotOverLine1Display.SelectionCellLabelOpacity = 1.0
    plotOverLine1Display.SelectionCellLabelShadow = 0
    plotOverLine1Display.SelectionPointLabelBold = 0
    plotOverLine1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    plotOverLine1Display.SelectionPointLabelFontFamily = 'Arial'
    plotOverLine1Display.SelectionPointLabelFontFile = ''
    plotOverLine1Display.SelectionPointLabelFontSize = 18
    plotOverLine1Display.SelectionPointLabelItalic = 0
    plotOverLine1Display.SelectionPointLabelJustification = 'Left'
    plotOverLine1Display.SelectionPointLabelOpacity = 1.0
    plotOverLine1Display.SelectionPointLabelShadow = 0
    plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    plotOverLine1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    plotOverLine1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    plotOverLine1Display.GlyphType.TipResolution = 6
    plotOverLine1Display.GlyphType.TipRadius = 0.1
    plotOverLine1Display.GlyphType.TipLength = 0.35
    plotOverLine1Display.GlyphType.ShaftResolution = 6
    plotOverLine1Display.GlyphType.ShaftRadius = 0.03
    plotOverLine1Display.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    plotOverLine1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3500.0, 1.0, 0.5, 0.0]
    plotOverLine1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    plotOverLine1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3500.0, 1.0, 0.5, 0.0]
    plotOverLine1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    plotOverLine1Display.DataAxesGrid.XTitle = 'X Axis'
    plotOverLine1Display.DataAxesGrid.YTitle = 'Y Axis'
    plotOverLine1Display.DataAxesGrid.ZTitle = 'Z Axis'
    plotOverLine1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.XTitleBold = 0
    plotOverLine1Display.DataAxesGrid.XTitleItalic = 0
    plotOverLine1Display.DataAxesGrid.XTitleFontSize = 12
    plotOverLine1Display.DataAxesGrid.XTitleShadow = 0
    plotOverLine1Display.DataAxesGrid.XTitleOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.YTitleBold = 0
    plotOverLine1Display.DataAxesGrid.YTitleItalic = 0
    plotOverLine1Display.DataAxesGrid.YTitleFontSize = 12
    plotOverLine1Display.DataAxesGrid.YTitleShadow = 0
    plotOverLine1Display.DataAxesGrid.YTitleOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
    plotOverLine1Display.DataAxesGrid.ZTitleBold = 0
    plotOverLine1Display.DataAxesGrid.ZTitleItalic = 0
    plotOverLine1Display.DataAxesGrid.ZTitleFontSize = 12
    plotOverLine1Display.DataAxesGrid.ZTitleShadow = 0
    plotOverLine1Display.DataAxesGrid.ZTitleOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.FacesToRender = 63
    plotOverLine1Display.DataAxesGrid.CullBackface = 0
    plotOverLine1Display.DataAxesGrid.CullFrontface = 1
    plotOverLine1Display.DataAxesGrid.ShowGrid = 0
    plotOverLine1Display.DataAxesGrid.ShowEdges = 1
    plotOverLine1Display.DataAxesGrid.ShowTicks = 1
    plotOverLine1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    plotOverLine1Display.DataAxesGrid.AxesToLabel = 63
    plotOverLine1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
    plotOverLine1Display.DataAxesGrid.XLabelBold = 0
    plotOverLine1Display.DataAxesGrid.XLabelItalic = 0
    plotOverLine1Display.DataAxesGrid.XLabelFontSize = 12
    plotOverLine1Display.DataAxesGrid.XLabelShadow = 0
    plotOverLine1Display.DataAxesGrid.XLabelOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
    plotOverLine1Display.DataAxesGrid.YLabelBold = 0
    plotOverLine1Display.DataAxesGrid.YLabelItalic = 0
    plotOverLine1Display.DataAxesGrid.YLabelFontSize = 12
    plotOverLine1Display.DataAxesGrid.YLabelShadow = 0
    plotOverLine1Display.DataAxesGrid.YLabelOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''
    plotOverLine1Display.DataAxesGrid.ZLabelBold = 0
    plotOverLine1Display.DataAxesGrid.ZLabelItalic = 0
    plotOverLine1Display.DataAxesGrid.ZLabelFontSize = 12
    plotOverLine1Display.DataAxesGrid.ZLabelShadow = 0
    plotOverLine1Display.DataAxesGrid.ZLabelOpacity = 1.0
    plotOverLine1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    plotOverLine1Display.DataAxesGrid.XAxisPrecision = 2
    plotOverLine1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    plotOverLine1Display.DataAxesGrid.XAxisLabels = []
    plotOverLine1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    plotOverLine1Display.DataAxesGrid.YAxisPrecision = 2
    plotOverLine1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    plotOverLine1Display.DataAxesGrid.YAxisLabels = []
    plotOverLine1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    plotOverLine1Display.DataAxesGrid.ZAxisPrecision = 2
    plotOverLine1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    plotOverLine1Display.DataAxesGrid.ZAxisLabels = []
    plotOverLine1Display.DataAxesGrid.UseCustomBounds = 0
    plotOverLine1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    plotOverLine1Display.PolarAxes.Visibility = 0
    plotOverLine1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    plotOverLine1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    plotOverLine1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    plotOverLine1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    plotOverLine1Display.PolarAxes.EnableCustomRange = 0
    plotOverLine1Display.PolarAxes.CustomRange = [0.0, 1.0]
    plotOverLine1Display.PolarAxes.PolarAxisVisibility = 1
    plotOverLine1Display.PolarAxes.RadialAxesVisibility = 1
    plotOverLine1Display.PolarAxes.DrawRadialGridlines = 1
    plotOverLine1Display.PolarAxes.PolarArcsVisibility = 1
    plotOverLine1Display.PolarAxes.DrawPolarArcsGridlines = 1
    plotOverLine1Display.PolarAxes.NumberOfRadialAxes = 0
    plotOverLine1Display.PolarAxes.AutoSubdividePolarAxis = 1
    plotOverLine1Display.PolarAxes.NumberOfPolarAxis = 0
    plotOverLine1Display.PolarAxes.MinimumRadius = 0.0
    plotOverLine1Display.PolarAxes.MinimumAngle = 0.0
    plotOverLine1Display.PolarAxes.MaximumAngle = 90.0
    plotOverLine1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    plotOverLine1Display.PolarAxes.Ratio = 1.0
    plotOverLine1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    plotOverLine1Display.PolarAxes.PolarAxisTitleVisibility = 1
    plotOverLine1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    plotOverLine1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    plotOverLine1Display.PolarAxes.PolarLabelVisibility = 1
    plotOverLine1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    plotOverLine1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    plotOverLine1Display.PolarAxes.RadialLabelVisibility = 1
    plotOverLine1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    plotOverLine1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    plotOverLine1Display.PolarAxes.RadialUnitsVisibility = 1
    plotOverLine1Display.PolarAxes.ScreenSize = 10.0
    plotOverLine1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    plotOverLine1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
    plotOverLine1Display.PolarAxes.PolarAxisTitleBold = 0
    plotOverLine1Display.PolarAxes.PolarAxisTitleItalic = 0
    plotOverLine1Display.PolarAxes.PolarAxisTitleShadow = 0
    plotOverLine1Display.PolarAxes.PolarAxisTitleFontSize = 12
    plotOverLine1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    plotOverLine1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
    plotOverLine1Display.PolarAxes.PolarAxisLabelBold = 0
    plotOverLine1Display.PolarAxes.PolarAxisLabelItalic = 0
    plotOverLine1Display.PolarAxes.PolarAxisLabelShadow = 0
    plotOverLine1Display.PolarAxes.PolarAxisLabelFontSize = 12
    plotOverLine1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    plotOverLine1Display.PolarAxes.LastRadialAxisTextBold = 0
    plotOverLine1Display.PolarAxes.LastRadialAxisTextItalic = 0
    plotOverLine1Display.PolarAxes.LastRadialAxisTextShadow = 0
    plotOverLine1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    plotOverLine1Display.PolarAxes.EnableDistanceLOD = 1
    plotOverLine1Display.PolarAxes.DistanceLODThreshold = 0.7
    plotOverLine1Display.PolarAxes.EnableViewAngleLOD = 1
    plotOverLine1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    plotOverLine1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    plotOverLine1Display.PolarAxes.PolarTicksVisibility = 1
    plotOverLine1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    plotOverLine1Display.PolarAxes.TickLocation = 'Both'
    plotOverLine1Display.PolarAxes.AxisTickVisibility = 1
    plotOverLine1Display.PolarAxes.AxisMinorTickVisibility = 0
    plotOverLine1Display.PolarAxes.ArcTickVisibility = 1
    plotOverLine1Display.PolarAxes.ArcMinorTickVisibility = 0
    plotOverLine1Display.PolarAxes.DeltaAngleMajor = 10.0
    plotOverLine1Display.PolarAxes.DeltaAngleMinor = 5.0
    plotOverLine1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    plotOverLine1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    plotOverLine1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    plotOverLine1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    plotOverLine1Display.PolarAxes.ArcMajorTickSize = 0.0
    plotOverLine1Display.PolarAxes.ArcTickRatioSize = 0.3
    plotOverLine1Display.PolarAxes.ArcMajorTickThickness = 1.0
    plotOverLine1Display.PolarAxes.ArcTickRatioThickness = 0.5
    plotOverLine1Display.PolarAxes.Use2DMode = 0
    plotOverLine1Display.PolarAxes.UseLogAxis = 0

    # Create a new 'Line Chart View'
    lineChartView1 = CreateView('XYChartView')
    lineChartView1.UseCache = 0
    lineChartView1.ViewSize = [400, 400]
    lineChartView1.ChartTitle = ''
    lineChartView1.ChartTitleAlignment = 'Center'
    lineChartView1.ChartTitleFontFamily = 'Arial'
    lineChartView1.ChartTitleFontFile = ''
    lineChartView1.ChartTitleFontSize = 18
    lineChartView1.ChartTitleBold = 0
    lineChartView1.ChartTitleItalic = 0
    lineChartView1.ChartTitleColor = [0.0, 0.0, 0.0]
    lineChartView1.ShowLegend = 1
    lineChartView1.LegendLocation = 'TopRight'
    lineChartView1.LegendSymbolWidth = 25
    lineChartView1.SortByXAxis = 0
    lineChartView1.LegendPosition = [0, 0]
    lineChartView1.LegendFontFamily = 'Arial'
    lineChartView1.LegendFontFile = ''
    lineChartView1.LegendFontSize = 12
    lineChartView1.LegendBold = 0
    lineChartView1.LegendItalic = 0
    lineChartView1.TooltipNotation = 'Mixed'
    lineChartView1.TooltipPrecision = 6
    lineChartView1.HideTimeMarker = 0
    lineChartView1.LeftAxisTitle = ''
    lineChartView1.ShowLeftAxisGrid = 1
    lineChartView1.LeftAxisGridColor = [0.95, 0.95, 0.95]
    lineChartView1.LeftAxisColor = [0.0, 0.0, 0.0]
    lineChartView1.LeftAxisTitleFontFamily = 'Arial'
    lineChartView1.LeftAxisTitleFontFile = ''
    lineChartView1.LeftAxisTitleFontSize = 18
    lineChartView1.LeftAxisTitleBold = 1
    lineChartView1.LeftAxisTitleItalic = 0
    lineChartView1.LeftAxisTitleColor = [0.0, 0.0, 0.0]
    lineChartView1.LeftAxisLogScale = 0
    lineChartView1.LeftAxisUseCustomRange = 0
    lineChartView1.LeftAxisRangeMinimum = 0.0
    lineChartView1.LeftAxisRangeMaximum = 1.0
    lineChartView1.ShowLeftAxisLabels = 1
    lineChartView1.LeftAxisLabelNotation = 'Mixed'
    lineChartView1.LeftAxisLabelPrecision = 2
    lineChartView1.LeftAxisUseCustomLabels = 0
    lineChartView1.LeftAxisLabels = []
    lineChartView1.LeftAxisLabelFontFamily = 'Arial'
    lineChartView1.LeftAxisLabelFontFile = ''
    lineChartView1.LeftAxisLabelFontSize = 12
    lineChartView1.LeftAxisLabelBold = 0
    lineChartView1.LeftAxisLabelItalic = 0
    lineChartView1.LeftAxisLabelColor = [0.0, 0.0, 0.0]
    lineChartView1.BottomAxisTitle = ''
    lineChartView1.ShowBottomAxisGrid = 1
    lineChartView1.BottomAxisGridColor = [0.95, 0.95, 0.95]
    lineChartView1.BottomAxisColor = [0.0, 0.0, 0.0]
    lineChartView1.BottomAxisTitleFontFamily = 'Arial'
    lineChartView1.BottomAxisTitleFontFile = ''
    lineChartView1.BottomAxisTitleFontSize = 18
    lineChartView1.BottomAxisTitleBold = 1
    lineChartView1.BottomAxisTitleItalic = 0
    lineChartView1.BottomAxisTitleColor = [0.0, 0.0, 0.0]
    lineChartView1.BottomAxisLogScale = 0
    lineChartView1.BottomAxisUseCustomRange = 0
    lineChartView1.BottomAxisRangeMinimum = 0.0
    lineChartView1.BottomAxisRangeMaximum = 1.0
    lineChartView1.ShowBottomAxisLabels = 1
    lineChartView1.BottomAxisLabelNotation = 'Mixed'
    lineChartView1.BottomAxisLabelPrecision = 2
    lineChartView1.BottomAxisUseCustomLabels = 0
    lineChartView1.BottomAxisLabels = []
    lineChartView1.BottomAxisLabelFontFamily = 'Arial'
    lineChartView1.BottomAxisLabelFontFile = ''
    lineChartView1.BottomAxisLabelFontSize = 12
    lineChartView1.BottomAxisLabelBold = 0
    lineChartView1.BottomAxisLabelItalic = 0
    lineChartView1.BottomAxisLabelColor = [0.0, 0.0, 0.0]
    lineChartView1.RightAxisTitle = ''
    lineChartView1.ShowRightAxisGrid = 1
    lineChartView1.RightAxisGridColor = [0.95, 0.95, 0.95]
    lineChartView1.RightAxisColor = [0.0, 0.0, 0.0]
    lineChartView1.RightAxisTitleFontFamily = 'Arial'
    lineChartView1.RightAxisTitleFontFile = ''
    lineChartView1.RightAxisTitleFontSize = 18
    lineChartView1.RightAxisTitleBold = 1
    lineChartView1.RightAxisTitleItalic = 0
    lineChartView1.RightAxisTitleColor = [0.0, 0.0, 0.0]
    lineChartView1.RightAxisLogScale = 0
    lineChartView1.RightAxisUseCustomRange = 0
    lineChartView1.RightAxisRangeMinimum = 0.0
    lineChartView1.RightAxisRangeMaximum = 1.0
    lineChartView1.ShowRightAxisLabels = 1
    lineChartView1.RightAxisLabelNotation = 'Mixed'
    lineChartView1.RightAxisLabelPrecision = 2
    lineChartView1.RightAxisUseCustomLabels = 0
    lineChartView1.RightAxisLabels = []
    lineChartView1.RightAxisLabelFontFamily = 'Arial'
    lineChartView1.RightAxisLabelFontFile = ''
    lineChartView1.RightAxisLabelFontSize = 12
    lineChartView1.RightAxisLabelBold = 0
    lineChartView1.RightAxisLabelItalic = 0
    lineChartView1.RightAxisLabelColor = [0.0, 0.0, 0.0]
    lineChartView1.TopAxisTitle = ''
    lineChartView1.ShowTopAxisGrid = 1
    lineChartView1.TopAxisGridColor = [0.95, 0.95, 0.95]
    lineChartView1.TopAxisColor = [0.0, 0.0, 0.0]
    lineChartView1.TopAxisTitleFontFamily = 'Arial'
    lineChartView1.TopAxisTitleFontFile = ''
    lineChartView1.TopAxisTitleFontSize = 18
    lineChartView1.TopAxisTitleBold = 1
    lineChartView1.TopAxisTitleItalic = 0
    lineChartView1.TopAxisTitleColor = [0.0, 0.0, 0.0]
    lineChartView1.TopAxisLogScale = 0
    lineChartView1.TopAxisUseCustomRange = 0
    lineChartView1.TopAxisRangeMinimum = 0.0
    lineChartView1.TopAxisRangeMaximum = 1.0
    lineChartView1.ShowTopAxisLabels = 1
    lineChartView1.TopAxisLabelNotation = 'Mixed'
    lineChartView1.TopAxisLabelPrecision = 2
    lineChartView1.TopAxisUseCustomLabels = 0
    lineChartView1.TopAxisLabels = []
    lineChartView1.TopAxisLabelFontFamily = 'Arial'
    lineChartView1.TopAxisLabelFontFile = ''
    lineChartView1.TopAxisLabelFontSize = 12
    lineChartView1.TopAxisLabelBold = 0
    lineChartView1.TopAxisLabelItalic = 0
    lineChartView1.TopAxisLabelColor = [0.0, 0.0, 0.0]

    # show data in view
    plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

    # trace defaults for the display properties.
    plotOverLine1Display_1.CompositeDataSetIndex = [1]
    plotOverLine1Display_1.AttributeType = 'Point Data'
    plotOverLine1Display_1.UseIndexForXAxis = 0
    plotOverLine1Display_1.XArrayName = 'arc_length'
    plotOverLine1Display_1.SeriesVisibility = ['f']
    plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'f', 'f', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
    plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'f', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0.5000076295109483', '0', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
    plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'f', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesLabelPrefix = ''
    plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'f', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'f', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'f', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'f', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

    # get layout
    layout1 = GetLayoutByName("Layout #1")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

    # Properties modified on plotOverLine1Display_1
    plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'f', '0', 'vtkValidPointMask', '0']
    plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'f', '1', 'vtkValidPointMask', '1']
    plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'f', '2', 'vtkValidPointMask', '2']
    plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'f', '0', 'vtkValidPointMask', '0']
    plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'f', '4', 'vtkValidPointMask', '4']

    # update the view to ensure updated data information
    lineChartView1.Update()

    # Make the directory
    directory = "strong_long_pumping"
      
    # Parent Directory path
    parent_dir = "../output/plots"
      
    # Path
    path = os.path.join(parent_dir, directory)
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
      # Create the directory
      os.mkdir(path)

    # save data
    SaveData(f'../output/plots/strong_long_pumping/{inputfile}_{direction}.csv', proxy=plotOverLine1, WriteTimeSteps=0,
        Filenamesuffix='_%d',
        ChooseArraysToWrite=1,
        PointDataArrays=['arc_length', 'f', 'vtkValidPointMask'],
        CellDataArrays=[],
        FieldDataArrays=[],
        VertexDataArrays=[],
        EdgeDataArrays=[],
        RowDataArrays=[],
        Precision=5,
        UseScientificNotation=0,
        FieldAssociation='Point Data',
        AddMetaData=1,
        AddTime=0)
    
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
  renderView1.CameraPosition = [1000.0, 1750.0, -7619.697272912243]
  renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
  renderView1.CameraViewUp = [0.5877852522924731, 0.8090169943749475, 0.0]
  renderView1.CameraParallelScale = 2026.4747716169575

  #--------------------------------------------
  # uncomment the following to render all views
  # RenderAllViews()
  # alternatively, if you want to write images, you can use SaveScreenshot(...).
