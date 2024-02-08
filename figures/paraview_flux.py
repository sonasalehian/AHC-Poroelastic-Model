# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters
import os

def extract_paraview_flux(direction, t):
  #### disable automatic camera reset on 'Show'
  paraview.simple._DisableFirstRenderCameraReset()

  # create a new 'ADIOS2VTXReader'
  fluxbp = ADIOS2VTXReader(registrationName='flux.bp', FileName='../output/AJ/flux.bp')

  # get animation scene
  animationScene1 = GetAnimationScene()

  # update animation scene based on data timesteps
  animationScene1.UpdateAnimationUsingDataTimeSteps()

  # get active view
  renderView1 = GetActiveViewOrCreate('RenderView')

  # show data in view
  fluxbpDisplay = Show(fluxbp, renderView1, 'UnstructuredGridRepresentation')

  # trace defaults for the display properties.
  fluxbpDisplay.Selection = None
  fluxbpDisplay.Representation = 'Surface'
  fluxbpDisplay.ColorArrayName = [None, '']
  fluxbpDisplay.LookupTable = None
  fluxbpDisplay.MapScalars = 1
  fluxbpDisplay.MultiComponentsMapping = 0
  fluxbpDisplay.InterpolateScalarsBeforeMapping = 1
  fluxbpDisplay.Opacity = 1.0
  fluxbpDisplay.PointSize = 2.0
  fluxbpDisplay.LineWidth = 1.0
  fluxbpDisplay.RenderLinesAsTubes = 0
  fluxbpDisplay.RenderPointsAsSpheres = 0
  fluxbpDisplay.Interpolation = 'Gouraud'
  fluxbpDisplay.Specular = 0.0
  fluxbpDisplay.SpecularColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.SpecularPower = 100.0
  fluxbpDisplay.Luminosity = 0.0
  fluxbpDisplay.Ambient = 0.0
  fluxbpDisplay.Diffuse = 1.0
  fluxbpDisplay.Roughness = 0.3
  fluxbpDisplay.Metallic = 0.0
  fluxbpDisplay.EdgeTint = [1.0, 1.0, 1.0]
  fluxbpDisplay.Anisotropy = 0.0
  fluxbpDisplay.AnisotropyRotation = 0.0
  fluxbpDisplay.BaseIOR = 1.5
  fluxbpDisplay.CoatStrength = 0.0
  fluxbpDisplay.CoatIOR = 2.0
  fluxbpDisplay.CoatRoughness = 0.0
  fluxbpDisplay.CoatColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.SelectTCoordArray = 'None'
  fluxbpDisplay.SelectNormalArray = 'None'
  fluxbpDisplay.SelectTangentArray = 'None'
  fluxbpDisplay.Texture = None
  fluxbpDisplay.RepeatTextures = 1
  fluxbpDisplay.InterpolateTextures = 0
  fluxbpDisplay.SeamlessU = 0
  fluxbpDisplay.SeamlessV = 0
  fluxbpDisplay.UseMipmapTextures = 0
  fluxbpDisplay.ShowTexturesOnBackface = 1
  fluxbpDisplay.BaseColorTexture = None
  fluxbpDisplay.NormalTexture = None
  fluxbpDisplay.NormalScale = 1.0
  fluxbpDisplay.CoatNormalTexture = None
  fluxbpDisplay.CoatNormalScale = 1.0
  fluxbpDisplay.MaterialTexture = None
  fluxbpDisplay.OcclusionStrength = 1.0
  fluxbpDisplay.AnisotropyTexture = None
  fluxbpDisplay.EmissiveTexture = None
  fluxbpDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
  fluxbpDisplay.FlipTextures = 0
  fluxbpDisplay.BackfaceRepresentation = 'Follow Frontface'
  fluxbpDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.BackfaceOpacity = 1.0
  fluxbpDisplay.Position = [0.0, 0.0, 0.0]
  fluxbpDisplay.Scale = [1.0, 1.0, 1.0]
  fluxbpDisplay.Orientation = [0.0, 0.0, 0.0]
  fluxbpDisplay.Origin = [0.0, 0.0, 0.0]
  fluxbpDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
  fluxbpDisplay.Pickable = 1
  fluxbpDisplay.Triangulate = 0
  fluxbpDisplay.UseShaderReplacements = 0
  fluxbpDisplay.ShaderReplacements = ''
  fluxbpDisplay.NonlinearSubdivisionLevel = 1
  fluxbpDisplay.UseDataPartitions = 0
  fluxbpDisplay.OSPRayUseScaleArray = 'All Approximate'
  fluxbpDisplay.OSPRayScaleArray = 'f'
  fluxbpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
  fluxbpDisplay.OSPRayMaterial = 'None'
  fluxbpDisplay.BlockSelectors = ['/']
  fluxbpDisplay.BlockColors = []
  fluxbpDisplay.BlockOpacities = []
  fluxbpDisplay.Orient = 0
  fluxbpDisplay.OrientationMode = 'Direction'
  fluxbpDisplay.SelectOrientationVectors = 'None'
  fluxbpDisplay.Scaling = 0
  fluxbpDisplay.ScaleMode = 'No Data Scaling Off'
  fluxbpDisplay.ScaleFactor = 350.00000000000006
  fluxbpDisplay.SelectScaleArray = 'None'
  fluxbpDisplay.GlyphType = 'Arrow'
  fluxbpDisplay.UseGlyphTable = 0
  fluxbpDisplay.GlyphTableIndexArray = 'None'
  fluxbpDisplay.UseCompositeGlyphTable = 0
  fluxbpDisplay.UseGlyphCullingAndLOD = 0
  fluxbpDisplay.LODValues = []
  fluxbpDisplay.ColorByLODIndex = 0
  fluxbpDisplay.GaussianRadius = 17.500000000000004
  fluxbpDisplay.ShaderPreset = 'Sphere'
  fluxbpDisplay.CustomTriangleScale = 3
  fluxbpDisplay.CustomShader = """ // This custom shader code define a gaussian blur
  // Please take a look into vtkSMPointGaussianRepresentation.cxx
  // for other custom shader examples
  //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
  """
  fluxbpDisplay.Emissive = 0
  fluxbpDisplay.ScaleByArray = 0
  fluxbpDisplay.SetScaleArray = ['POINTS', 'f']
  fluxbpDisplay.ScaleArrayComponent = 'X'
  fluxbpDisplay.UseScaleFunction = 1
  fluxbpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
  fluxbpDisplay.OpacityByArray = 0
  fluxbpDisplay.OpacityArray = ['POINTS', 'f']
  fluxbpDisplay.OpacityArrayComponent = 'X'
  fluxbpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
  fluxbpDisplay.DataAxesGrid = 'GridAxesRepresentation'
  fluxbpDisplay.SelectionCellLabelBold = 0
  fluxbpDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
  fluxbpDisplay.SelectionCellLabelFontFamily = 'Arial'
  fluxbpDisplay.SelectionCellLabelFontFile = ''
  fluxbpDisplay.SelectionCellLabelFontSize = 18
  fluxbpDisplay.SelectionCellLabelItalic = 0
  fluxbpDisplay.SelectionCellLabelJustification = 'Left'
  fluxbpDisplay.SelectionCellLabelOpacity = 1.0
  fluxbpDisplay.SelectionCellLabelShadow = 0
  fluxbpDisplay.SelectionPointLabelBold = 0
  fluxbpDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
  fluxbpDisplay.SelectionPointLabelFontFamily = 'Arial'
  fluxbpDisplay.SelectionPointLabelFontFile = ''
  fluxbpDisplay.SelectionPointLabelFontSize = 18
  fluxbpDisplay.SelectionPointLabelItalic = 0
  fluxbpDisplay.SelectionPointLabelJustification = 'Left'
  fluxbpDisplay.SelectionPointLabelOpacity = 1.0
  fluxbpDisplay.SelectionPointLabelShadow = 0
  fluxbpDisplay.PolarAxes = 'PolarAxesRepresentation'
  fluxbpDisplay.ScalarOpacityFunction = None
  fluxbpDisplay.ScalarOpacityUnitDistance = 60.29637080930927
  fluxbpDisplay.UseSeparateOpacityArray = 0
  fluxbpDisplay.OpacityArrayName = ['POINTS', 'f']
  fluxbpDisplay.OpacityComponent = 'X'
  fluxbpDisplay.SelectMapper = 'Projected tetra'
  fluxbpDisplay.SamplingDimensions = [128, 128, 128]
  fluxbpDisplay.UseFloatingPointFrameBuffer = 1

  # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
  fluxbpDisplay.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
  fluxbpDisplay.OSPRayScaleFunction.UseLogScale = 0

  # init the 'Arrow' selected for 'GlyphType'
  fluxbpDisplay.GlyphType.TipResolution = 6
  fluxbpDisplay.GlyphType.TipRadius = 0.1
  fluxbpDisplay.GlyphType.TipLength = 0.35
  fluxbpDisplay.GlyphType.ShaftResolution = 6
  fluxbpDisplay.GlyphType.ShaftRadius = 0.03
  fluxbpDisplay.GlyphType.Invert = 0

  # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
  fluxbpDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  fluxbpDisplay.ScaleTransferFunction.UseLogScale = 0

  # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
  fluxbpDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  fluxbpDisplay.OpacityTransferFunction.UseLogScale = 0

  # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
  fluxbpDisplay.DataAxesGrid.XTitle = 'X Axis'
  fluxbpDisplay.DataAxesGrid.YTitle = 'Y Axis'
  fluxbpDisplay.DataAxesGrid.ZTitle = 'Z Axis'
  fluxbpDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.XTitleFontFile = ''
  fluxbpDisplay.DataAxesGrid.XTitleBold = 0
  fluxbpDisplay.DataAxesGrid.XTitleItalic = 0
  fluxbpDisplay.DataAxesGrid.XTitleFontSize = 12
  fluxbpDisplay.DataAxesGrid.XTitleShadow = 0
  fluxbpDisplay.DataAxesGrid.XTitleOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.YTitleFontFile = ''
  fluxbpDisplay.DataAxesGrid.YTitleBold = 0
  fluxbpDisplay.DataAxesGrid.YTitleItalic = 0
  fluxbpDisplay.DataAxesGrid.YTitleFontSize = 12
  fluxbpDisplay.DataAxesGrid.YTitleShadow = 0
  fluxbpDisplay.DataAxesGrid.YTitleOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.ZTitleFontFile = ''
  fluxbpDisplay.DataAxesGrid.ZTitleBold = 0
  fluxbpDisplay.DataAxesGrid.ZTitleItalic = 0
  fluxbpDisplay.DataAxesGrid.ZTitleFontSize = 12
  fluxbpDisplay.DataAxesGrid.ZTitleShadow = 0
  fluxbpDisplay.DataAxesGrid.ZTitleOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.FacesToRender = 63
  fluxbpDisplay.DataAxesGrid.CullBackface = 0
  fluxbpDisplay.DataAxesGrid.CullFrontface = 1
  fluxbpDisplay.DataAxesGrid.ShowGrid = 0
  fluxbpDisplay.DataAxesGrid.ShowEdges = 1
  fluxbpDisplay.DataAxesGrid.ShowTicks = 1
  fluxbpDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
  fluxbpDisplay.DataAxesGrid.AxesToLabel = 63
  fluxbpDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.XLabelFontFile = ''
  fluxbpDisplay.DataAxesGrid.XLabelBold = 0
  fluxbpDisplay.DataAxesGrid.XLabelItalic = 0
  fluxbpDisplay.DataAxesGrid.XLabelFontSize = 12
  fluxbpDisplay.DataAxesGrid.XLabelShadow = 0
  fluxbpDisplay.DataAxesGrid.XLabelOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.YLabelFontFile = ''
  fluxbpDisplay.DataAxesGrid.YLabelBold = 0
  fluxbpDisplay.DataAxesGrid.YLabelItalic = 0
  fluxbpDisplay.DataAxesGrid.YLabelFontSize = 12
  fluxbpDisplay.DataAxesGrid.YLabelShadow = 0
  fluxbpDisplay.DataAxesGrid.YLabelOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
  fluxbpDisplay.DataAxesGrid.ZLabelFontFile = ''
  fluxbpDisplay.DataAxesGrid.ZLabelBold = 0
  fluxbpDisplay.DataAxesGrid.ZLabelItalic = 0
  fluxbpDisplay.DataAxesGrid.ZLabelFontSize = 12
  fluxbpDisplay.DataAxesGrid.ZLabelShadow = 0
  fluxbpDisplay.DataAxesGrid.ZLabelOpacity = 1.0
  fluxbpDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
  fluxbpDisplay.DataAxesGrid.XAxisPrecision = 2
  fluxbpDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
  fluxbpDisplay.DataAxesGrid.XAxisLabels = []
  fluxbpDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
  fluxbpDisplay.DataAxesGrid.YAxisPrecision = 2
  fluxbpDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
  fluxbpDisplay.DataAxesGrid.YAxisLabels = []
  fluxbpDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
  fluxbpDisplay.DataAxesGrid.ZAxisPrecision = 2
  fluxbpDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
  fluxbpDisplay.DataAxesGrid.ZAxisLabels = []
  fluxbpDisplay.DataAxesGrid.UseCustomBounds = 0
  fluxbpDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

  # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
  fluxbpDisplay.PolarAxes.Visibility = 0
  fluxbpDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
  fluxbpDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
  fluxbpDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
  fluxbpDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
  fluxbpDisplay.PolarAxes.EnableCustomRange = 0
  fluxbpDisplay.PolarAxes.CustomRange = [0.0, 1.0]
  fluxbpDisplay.PolarAxes.PolarAxisVisibility = 1
  fluxbpDisplay.PolarAxes.RadialAxesVisibility = 1
  fluxbpDisplay.PolarAxes.DrawRadialGridlines = 1
  fluxbpDisplay.PolarAxes.PolarArcsVisibility = 1
  fluxbpDisplay.PolarAxes.DrawPolarArcsGridlines = 1
  fluxbpDisplay.PolarAxes.NumberOfRadialAxes = 0
  fluxbpDisplay.PolarAxes.AutoSubdividePolarAxis = 1
  fluxbpDisplay.PolarAxes.NumberOfPolarAxis = 0
  fluxbpDisplay.PolarAxes.MinimumRadius = 0.0
  fluxbpDisplay.PolarAxes.MinimumAngle = 0.0
  fluxbpDisplay.PolarAxes.MaximumAngle = 90.0
  fluxbpDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
  fluxbpDisplay.PolarAxes.Ratio = 1.0
  fluxbpDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
  fluxbpDisplay.PolarAxes.PolarAxisTitleVisibility = 1
  fluxbpDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
  fluxbpDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
  fluxbpDisplay.PolarAxes.PolarLabelVisibility = 1
  fluxbpDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
  fluxbpDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
  fluxbpDisplay.PolarAxes.RadialLabelVisibility = 1
  fluxbpDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
  fluxbpDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
  fluxbpDisplay.PolarAxes.RadialUnitsVisibility = 1
  fluxbpDisplay.PolarAxes.ScreenSize = 10.0
  fluxbpDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
  fluxbpDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
  fluxbpDisplay.PolarAxes.PolarAxisTitleFontFile = ''
  fluxbpDisplay.PolarAxes.PolarAxisTitleBold = 0
  fluxbpDisplay.PolarAxes.PolarAxisTitleItalic = 0
  fluxbpDisplay.PolarAxes.PolarAxisTitleShadow = 0
  fluxbpDisplay.PolarAxes.PolarAxisTitleFontSize = 12
  fluxbpDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
  fluxbpDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
  fluxbpDisplay.PolarAxes.PolarAxisLabelFontFile = ''
  fluxbpDisplay.PolarAxes.PolarAxisLabelBold = 0
  fluxbpDisplay.PolarAxes.PolarAxisLabelItalic = 0
  fluxbpDisplay.PolarAxes.PolarAxisLabelShadow = 0
  fluxbpDisplay.PolarAxes.PolarAxisLabelFontSize = 12
  fluxbpDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
  fluxbpDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
  fluxbpDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
  fluxbpDisplay.PolarAxes.LastRadialAxisTextBold = 0
  fluxbpDisplay.PolarAxes.LastRadialAxisTextItalic = 0
  fluxbpDisplay.PolarAxes.LastRadialAxisTextShadow = 0
  fluxbpDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
  fluxbpDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
  fluxbpDisplay.PolarAxes.EnableDistanceLOD = 1
  fluxbpDisplay.PolarAxes.DistanceLODThreshold = 0.7
  fluxbpDisplay.PolarAxes.EnableViewAngleLOD = 1
  fluxbpDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
  fluxbpDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
  fluxbpDisplay.PolarAxes.PolarTicksVisibility = 1
  fluxbpDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
  fluxbpDisplay.PolarAxes.TickLocation = 'Both'
  fluxbpDisplay.PolarAxes.AxisTickVisibility = 1
  fluxbpDisplay.PolarAxes.AxisMinorTickVisibility = 0
  fluxbpDisplay.PolarAxes.ArcTickVisibility = 1
  fluxbpDisplay.PolarAxes.ArcMinorTickVisibility = 0
  fluxbpDisplay.PolarAxes.DeltaAngleMajor = 10.0
  fluxbpDisplay.PolarAxes.DeltaAngleMinor = 5.0
  fluxbpDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
  fluxbpDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
  fluxbpDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
  fluxbpDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
  fluxbpDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
  fluxbpDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
  fluxbpDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
  fluxbpDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
  fluxbpDisplay.PolarAxes.ArcMajorTickSize = 0.0
  fluxbpDisplay.PolarAxes.ArcTickRatioSize = 0.3
  fluxbpDisplay.PolarAxes.ArcMajorTickThickness = 1.0
  fluxbpDisplay.PolarAxes.ArcTickRatioThickness = 0.5
  fluxbpDisplay.PolarAxes.Use2DMode = 0
  fluxbpDisplay.PolarAxes.UseLogAxis = 0

  # reset view to fit data
  renderView1.ResetCamera(False)

  # get the material library
  materialLibrary1 = GetMaterialLibrary()

  # update the view to ensure updated data information
  renderView1.Update()

  # set scalar coloring
  ColorBy(fluxbpDisplay, ('POINTS', 'f', 'Magnitude'))

  # rescale color and/or opacity maps used to include current data range
  fluxbpDisplay.RescaleTransferFunctionToDataRange(True, False)

  # show color bar/color legend
  fluxbpDisplay.SetScalarBarVisibility(renderView1, True)

  # get color transfer function/color map for 'f'
  fLUT = GetColorTransferFunction('f')

  # get opacity transfer function/opacity map for 'f'
  fPWF = GetOpacityTransferFunction('f')

  # create a new 'Calculator'
  calculator1 = Calculator(registrationName='Calculator1', Input=fluxbp)
  calculator1.AttributeType = 'Point Data'
  calculator1.CoordinateResults = 0
  calculator1.ResultNormals = 0
  calculator1.ResultTCoords = 0
  calculator1.ResultArrayName = 'Result'
  calculator1.Function = ''
  calculator1.ReplaceInvalidResults = 1
  calculator1.ReplacementValue = 0.0
  calculator1.ResultArrayType = 'Double'

  # Properties modified on calculator1
  calculator1.Function = 'log(abs(f+10^(-13))*10^13)'

  # show data in view
  calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

  # trace defaults for the display properties.
  calculator1Display.Selection = None
  calculator1Display.Representation = 'Surface'
  calculator1Display.ColorArrayName = ['POINTS', 'f']
  calculator1Display.LookupTable = fLUT
  calculator1Display.MapScalars = 1
  calculator1Display.MultiComponentsMapping = 0
  calculator1Display.InterpolateScalarsBeforeMapping = 1
  calculator1Display.Opacity = 1.0
  calculator1Display.PointSize = 2.0
  calculator1Display.LineWidth = 1.0
  calculator1Display.RenderLinesAsTubes = 0
  calculator1Display.RenderPointsAsSpheres = 0
  calculator1Display.Interpolation = 'Gouraud'
  calculator1Display.Specular = 0.0
  calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
  calculator1Display.SpecularPower = 100.0
  calculator1Display.Luminosity = 0.0
  calculator1Display.Ambient = 0.0
  calculator1Display.Diffuse = 1.0
  calculator1Display.Roughness = 0.3
  calculator1Display.Metallic = 0.0
  calculator1Display.EdgeTint = [1.0, 1.0, 1.0]
  calculator1Display.Anisotropy = 0.0
  calculator1Display.AnisotropyRotation = 0.0
  calculator1Display.BaseIOR = 1.5
  calculator1Display.CoatStrength = 0.0
  calculator1Display.CoatIOR = 2.0
  calculator1Display.CoatRoughness = 0.0
  calculator1Display.CoatColor = [1.0, 1.0, 1.0]
  calculator1Display.SelectTCoordArray = 'None'
  calculator1Display.SelectNormalArray = 'None'
  calculator1Display.SelectTangentArray = 'None'
  calculator1Display.Texture = None
  calculator1Display.RepeatTextures = 1
  calculator1Display.InterpolateTextures = 0
  calculator1Display.SeamlessU = 0
  calculator1Display.SeamlessV = 0
  calculator1Display.UseMipmapTextures = 0
  calculator1Display.ShowTexturesOnBackface = 1
  calculator1Display.BaseColorTexture = None
  calculator1Display.NormalTexture = None
  calculator1Display.NormalScale = 1.0
  calculator1Display.CoatNormalTexture = None
  calculator1Display.CoatNormalScale = 1.0
  calculator1Display.MaterialTexture = None
  calculator1Display.OcclusionStrength = 1.0
  calculator1Display.AnisotropyTexture = None
  calculator1Display.EmissiveTexture = None
  calculator1Display.EmissiveFactor = [1.0, 1.0, 1.0]
  calculator1Display.FlipTextures = 0
  calculator1Display.BackfaceRepresentation = 'Follow Frontface'
  calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
  calculator1Display.BackfaceOpacity = 1.0
  calculator1Display.Position = [0.0, 0.0, 0.0]
  calculator1Display.Scale = [1.0, 1.0, 1.0]
  calculator1Display.Orientation = [0.0, 0.0, 0.0]
  calculator1Display.Origin = [0.0, 0.0, 0.0]
  calculator1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
  calculator1Display.Pickable = 1
  calculator1Display.Triangulate = 0
  calculator1Display.UseShaderReplacements = 0
  calculator1Display.ShaderReplacements = ''
  calculator1Display.NonlinearSubdivisionLevel = 1
  calculator1Display.UseDataPartitions = 0
  calculator1Display.OSPRayUseScaleArray = 'All Approximate'
  calculator1Display.OSPRayScaleArray = 'Result'
  calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
  calculator1Display.OSPRayMaterial = 'None'
  calculator1Display.BlockSelectors = ['/']
  calculator1Display.BlockColors = []
  calculator1Display.BlockOpacities = []
  calculator1Display.Orient = 0
  calculator1Display.OrientationMode = 'Direction'
  calculator1Display.SelectOrientationVectors = 'Result'
  calculator1Display.Scaling = 0
  calculator1Display.ScaleMode = 'No Data Scaling Off'
  calculator1Display.ScaleFactor = 350.00000000000006
  calculator1Display.SelectScaleArray = 'None'
  calculator1Display.GlyphType = 'Arrow'
  calculator1Display.UseGlyphTable = 0
  calculator1Display.GlyphTableIndexArray = 'None'
  calculator1Display.UseCompositeGlyphTable = 0
  calculator1Display.UseGlyphCullingAndLOD = 0
  calculator1Display.LODValues = []
  calculator1Display.ColorByLODIndex = 0
  calculator1Display.GaussianRadius = 17.500000000000004
  calculator1Display.ShaderPreset = 'Sphere'
  calculator1Display.CustomTriangleScale = 3
  calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
  // Please take a look into vtkSMPointGaussianRepresentation.cxx
  // for other custom shader examples
  //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
  """
  calculator1Display.Emissive = 0
  calculator1Display.ScaleByArray = 0
  calculator1Display.SetScaleArray = ['POINTS', 'Result']
  calculator1Display.ScaleArrayComponent = 'X'
  calculator1Display.UseScaleFunction = 1
  calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
  calculator1Display.OpacityByArray = 0
  calculator1Display.OpacityArray = ['POINTS', 'Result']
  calculator1Display.OpacityArrayComponent = 'X'
  calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
  calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
  calculator1Display.SelectionCellLabelBold = 0
  calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
  calculator1Display.SelectionCellLabelFontFamily = 'Arial'
  calculator1Display.SelectionCellLabelFontFile = ''
  calculator1Display.SelectionCellLabelFontSize = 18
  calculator1Display.SelectionCellLabelItalic = 0
  calculator1Display.SelectionCellLabelJustification = 'Left'
  calculator1Display.SelectionCellLabelOpacity = 1.0
  calculator1Display.SelectionCellLabelShadow = 0
  calculator1Display.SelectionPointLabelBold = 0
  calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
  calculator1Display.SelectionPointLabelFontFamily = 'Arial'
  calculator1Display.SelectionPointLabelFontFile = ''
  calculator1Display.SelectionPointLabelFontSize = 18
  calculator1Display.SelectionPointLabelItalic = 0
  calculator1Display.SelectionPointLabelJustification = 'Left'
  calculator1Display.SelectionPointLabelOpacity = 1.0
  calculator1Display.SelectionPointLabelShadow = 0
  calculator1Display.PolarAxes = 'PolarAxesRepresentation'
  calculator1Display.ScalarOpacityFunction = fPWF
  calculator1Display.ScalarOpacityUnitDistance = 60.29637080930927
  calculator1Display.UseSeparateOpacityArray = 0
  calculator1Display.OpacityArrayName = ['POINTS', 'Result']
  calculator1Display.OpacityComponent = 'X'
  calculator1Display.SelectMapper = 'Projected tetra'
  calculator1Display.SamplingDimensions = [128, 128, 128]
  calculator1Display.UseFloatingPointFrameBuffer = 1

  # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
  calculator1Display.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
  calculator1Display.OSPRayScaleFunction.UseLogScale = 0

  # init the 'Arrow' selected for 'GlyphType'
  calculator1Display.GlyphType.TipResolution = 6
  calculator1Display.GlyphType.TipRadius = 0.1
  calculator1Display.GlyphType.TipLength = 0.35
  calculator1Display.GlyphType.ShaftResolution = 6
  calculator1Display.GlyphType.ShaftRadius = 0.03
  calculator1Display.GlyphType.Invert = 0

  # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
  calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  calculator1Display.ScaleTransferFunction.UseLogScale = 0

  # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
  calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
  calculator1Display.OpacityTransferFunction.UseLogScale = 0

  # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
  calculator1Display.DataAxesGrid.XTitle = 'X Axis'
  calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
  calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
  calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.XTitleFontFile = ''
  calculator1Display.DataAxesGrid.XTitleBold = 0
  calculator1Display.DataAxesGrid.XTitleItalic = 0
  calculator1Display.DataAxesGrid.XTitleFontSize = 12
  calculator1Display.DataAxesGrid.XTitleShadow = 0
  calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
  calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.YTitleFontFile = ''
  calculator1Display.DataAxesGrid.YTitleBold = 0
  calculator1Display.DataAxesGrid.YTitleItalic = 0
  calculator1Display.DataAxesGrid.YTitleFontSize = 12
  calculator1Display.DataAxesGrid.YTitleShadow = 0
  calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
  calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.ZTitleFontFile = ''
  calculator1Display.DataAxesGrid.ZTitleBold = 0
  calculator1Display.DataAxesGrid.ZTitleItalic = 0
  calculator1Display.DataAxesGrid.ZTitleFontSize = 12
  calculator1Display.DataAxesGrid.ZTitleShadow = 0
  calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
  calculator1Display.DataAxesGrid.FacesToRender = 63
  calculator1Display.DataAxesGrid.CullBackface = 0
  calculator1Display.DataAxesGrid.CullFrontface = 1
  calculator1Display.DataAxesGrid.ShowGrid = 0
  calculator1Display.DataAxesGrid.ShowEdges = 1
  calculator1Display.DataAxesGrid.ShowTicks = 1
  calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
  calculator1Display.DataAxesGrid.AxesToLabel = 63
  calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.XLabelFontFile = ''
  calculator1Display.DataAxesGrid.XLabelBold = 0
  calculator1Display.DataAxesGrid.XLabelItalic = 0
  calculator1Display.DataAxesGrid.XLabelFontSize = 12
  calculator1Display.DataAxesGrid.XLabelShadow = 0
  calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
  calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.YLabelFontFile = ''
  calculator1Display.DataAxesGrid.YLabelBold = 0
  calculator1Display.DataAxesGrid.YLabelItalic = 0
  calculator1Display.DataAxesGrid.YLabelFontSize = 12
  calculator1Display.DataAxesGrid.YLabelShadow = 0
  calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
  calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
  calculator1Display.DataAxesGrid.ZLabelFontFile = ''
  calculator1Display.DataAxesGrid.ZLabelBold = 0
  calculator1Display.DataAxesGrid.ZLabelItalic = 0
  calculator1Display.DataAxesGrid.ZLabelFontSize = 12
  calculator1Display.DataAxesGrid.ZLabelShadow = 0
  calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
  calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
  calculator1Display.DataAxesGrid.XAxisPrecision = 2
  calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
  calculator1Display.DataAxesGrid.XAxisLabels = []
  calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
  calculator1Display.DataAxesGrid.YAxisPrecision = 2
  calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
  calculator1Display.DataAxesGrid.YAxisLabels = []
  calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
  calculator1Display.DataAxesGrid.ZAxisPrecision = 2
  calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
  calculator1Display.DataAxesGrid.ZAxisLabels = []
  calculator1Display.DataAxesGrid.UseCustomBounds = 0
  calculator1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

  # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
  calculator1Display.PolarAxes.Visibility = 0
  calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
  calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
  calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
  calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
  calculator1Display.PolarAxes.EnableCustomRange = 0
  calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
  calculator1Display.PolarAxes.PolarAxisVisibility = 1
  calculator1Display.PolarAxes.RadialAxesVisibility = 1
  calculator1Display.PolarAxes.DrawRadialGridlines = 1
  calculator1Display.PolarAxes.PolarArcsVisibility = 1
  calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
  calculator1Display.PolarAxes.NumberOfRadialAxes = 0
  calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
  calculator1Display.PolarAxes.NumberOfPolarAxis = 0
  calculator1Display.PolarAxes.MinimumRadius = 0.0
  calculator1Display.PolarAxes.MinimumAngle = 0.0
  calculator1Display.PolarAxes.MaximumAngle = 90.0
  calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
  calculator1Display.PolarAxes.Ratio = 1.0
  calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
  calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
  calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
  calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
  calculator1Display.PolarAxes.PolarLabelVisibility = 1
  calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
  calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
  calculator1Display.PolarAxes.RadialLabelVisibility = 1
  calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
  calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
  calculator1Display.PolarAxes.RadialUnitsVisibility = 1
  calculator1Display.PolarAxes.ScreenSize = 10.0
  calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
  calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
  calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
  calculator1Display.PolarAxes.PolarAxisTitleBold = 0
  calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
  calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
  calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
  calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
  calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
  calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
  calculator1Display.PolarAxes.PolarAxisLabelBold = 0
  calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
  calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
  calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
  calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
  calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
  calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
  calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
  calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
  calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
  calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
  calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
  calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
  calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
  calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
  calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
  calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
  calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
  calculator1Display.PolarAxes.EnableDistanceLOD = 1
  calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
  calculator1Display.PolarAxes.EnableViewAngleLOD = 1
  calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
  calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
  calculator1Display.PolarAxes.PolarTicksVisibility = 1
  calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
  calculator1Display.PolarAxes.TickLocation = 'Both'
  calculator1Display.PolarAxes.AxisTickVisibility = 1
  calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
  calculator1Display.PolarAxes.ArcTickVisibility = 1
  calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
  calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
  calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
  calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
  calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
  calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
  calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
  calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
  calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
  calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
  calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
  calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
  calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
  calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
  calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
  calculator1Display.PolarAxes.Use2DMode = 0
  calculator1Display.PolarAxes.UseLogAxis = 0

  # hide data in view
  Hide(fluxbp, renderView1)

  # show color bar/color legend
  calculator1Display.SetScalarBarVisibility(renderView1, True)

  # update the view to ensure updated data information
  renderView1.Update()

  if (direction == 'x'):
    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=calculator1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.UseDual = 0
    slice1.Crinkleslice = 0
    slice1.Triangulatetheslice = 1
    slice1.Mergeduplicatedpointsintheslice = 1
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [1000.0000000000001, 1750.0000000000002, 200.00000000000003]
    slice1.SliceType.Normal = [1.0, 0.0, 0.0]
    slice1.SliceType.Offset = 0.0

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [1000.0000000000001, 1750.0000000000002, 200.00000000000003]
    slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]
    slice1.HyperTreeGridSlicer.Offset = 0.0

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [750.0, 1750.0000000000002, 200.00000000000003]

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Selection = None
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'f']
    slice1Display.LookupTable = fLUT
    slice1Display.MapScalars = 1
    slice1Display.MultiComponentsMapping = 0
    slice1Display.InterpolateScalarsBeforeMapping = 1
    slice1Display.Opacity = 1.0
    slice1Display.PointSize = 2.0
    slice1Display.LineWidth = 1.0
    slice1Display.RenderLinesAsTubes = 0
    slice1Display.RenderPointsAsSpheres = 0
    slice1Display.Interpolation = 'Gouraud'
    slice1Display.Specular = 0.0
    slice1Display.SpecularColor = [1.0, 1.0, 1.0]
    slice1Display.SpecularPower = 100.0
    slice1Display.Luminosity = 0.0
    slice1Display.Ambient = 0.0
    slice1Display.Diffuse = 1.0
    slice1Display.Roughness = 0.3
    slice1Display.Metallic = 0.0
    slice1Display.EdgeTint = [1.0, 1.0, 1.0]
    slice1Display.Anisotropy = 0.0
    slice1Display.AnisotropyRotation = 0.0
    slice1Display.BaseIOR = 1.5
    slice1Display.CoatStrength = 0.0
    slice1Display.CoatIOR = 2.0
    slice1Display.CoatRoughness = 0.0
    slice1Display.CoatColor = [1.0, 1.0, 1.0]
    slice1Display.SelectTCoordArray = 'None'
    slice1Display.SelectNormalArray = 'None'
    slice1Display.SelectTangentArray = 'None'
    slice1Display.Texture = None
    slice1Display.RepeatTextures = 1
    slice1Display.InterpolateTextures = 0
    slice1Display.SeamlessU = 0
    slice1Display.SeamlessV = 0
    slice1Display.UseMipmapTextures = 0
    slice1Display.ShowTexturesOnBackface = 1
    slice1Display.BaseColorTexture = None
    slice1Display.NormalTexture = None
    slice1Display.NormalScale = 1.0
    slice1Display.CoatNormalTexture = None
    slice1Display.CoatNormalScale = 1.0
    slice1Display.MaterialTexture = None
    slice1Display.OcclusionStrength = 1.0
    slice1Display.AnisotropyTexture = None
    slice1Display.EmissiveTexture = None
    slice1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    slice1Display.FlipTextures = 0
    slice1Display.BackfaceRepresentation = 'Follow Frontface'
    slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    slice1Display.BackfaceOpacity = 1.0
    slice1Display.Position = [0.0, 0.0, 0.0]
    slice1Display.Scale = [1.0, 1.0, 1.0]
    slice1Display.Orientation = [0.0, 0.0, 0.0]
    slice1Display.Origin = [0.0, 0.0, 0.0]
    slice1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    slice1Display.Pickable = 1
    slice1Display.Triangulate = 0
    slice1Display.UseShaderReplacements = 0
    slice1Display.ShaderReplacements = ''
    slice1Display.NonlinearSubdivisionLevel = 1
    slice1Display.UseDataPartitions = 0
    slice1Display.OSPRayUseScaleArray = 'All Approximate'
    slice1Display.OSPRayScaleArray = 'Result'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.OSPRayMaterial = 'None'
    slice1Display.BlockSelectors = ['/']
    slice1Display.BlockColors = []
    slice1Display.BlockOpacities = []
    slice1Display.Orient = 0
    slice1Display.OrientationMode = 'Direction'
    slice1Display.SelectOrientationVectors = 'Result'
    slice1Display.Scaling = 0
    slice1Display.ScaleMode = 'No Data Scaling Off'
    slice1Display.ScaleFactor = 350.00000000000006
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.UseGlyphTable = 0
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.UseCompositeGlyphTable = 0
    slice1Display.UseGlyphCullingAndLOD = 0
    slice1Display.LODValues = []
    slice1Display.ColorByLODIndex = 0
    slice1Display.GaussianRadius = 17.500000000000004
    slice1Display.ShaderPreset = 'Sphere'
    slice1Display.CustomTriangleScale = 3
    slice1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    slice1Display.Emissive = 0
    slice1Display.ScaleByArray = 0
    slice1Display.SetScaleArray = ['POINTS', 'Result']
    slice1Display.ScaleArrayComponent = 'X'
    slice1Display.UseScaleFunction = 1
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityByArray = 0
    slice1Display.OpacityArray = ['POINTS', 'Result']
    slice1Display.OpacityArrayComponent = 'X'
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.SelectionCellLabelBold = 0
    slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    slice1Display.SelectionCellLabelFontFamily = 'Arial'
    slice1Display.SelectionCellLabelFontFile = ''
    slice1Display.SelectionCellLabelFontSize = 18
    slice1Display.SelectionCellLabelItalic = 0
    slice1Display.SelectionCellLabelJustification = 'Left'
    slice1Display.SelectionCellLabelOpacity = 1.0
    slice1Display.SelectionCellLabelShadow = 0
    slice1Display.SelectionPointLabelBold = 0
    slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    slice1Display.SelectionPointLabelFontFamily = 'Arial'
    slice1Display.SelectionPointLabelFontFile = ''
    slice1Display.SelectionPointLabelFontSize = 18
    slice1Display.SelectionPointLabelItalic = 0
    slice1Display.SelectionPointLabelJustification = 'Left'
    slice1Display.SelectionPointLabelOpacity = 1.0
    slice1Display.SelectionPointLabelShadow = 0
    slice1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    slice1Display.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
    slice1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    slice1Display.GlyphType.TipResolution = 6
    slice1Display.GlyphType.TipRadius = 0.1
    slice1Display.GlyphType.TipLength = 0.35
    slice1Display.GlyphType.ShaftResolution = 6
    slice1Display.GlyphType.ShaftRadius = 0.03
    slice1Display.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    slice1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    slice1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice1Display.DataAxesGrid.XTitle = 'X Axis'
    slice1Display.DataAxesGrid.YTitle = 'Y Axis'
    slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
    slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.XTitleFontFile = ''
    slice1Display.DataAxesGrid.XTitleBold = 0
    slice1Display.DataAxesGrid.XTitleItalic = 0
    slice1Display.DataAxesGrid.XTitleFontSize = 12
    slice1Display.DataAxesGrid.XTitleShadow = 0
    slice1Display.DataAxesGrid.XTitleOpacity = 1.0
    slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.YTitleFontFile = ''
    slice1Display.DataAxesGrid.YTitleBold = 0
    slice1Display.DataAxesGrid.YTitleItalic = 0
    slice1Display.DataAxesGrid.YTitleFontSize = 12
    slice1Display.DataAxesGrid.YTitleShadow = 0
    slice1Display.DataAxesGrid.YTitleOpacity = 1.0
    slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.ZTitleFontFile = ''
    slice1Display.DataAxesGrid.ZTitleBold = 0
    slice1Display.DataAxesGrid.ZTitleItalic = 0
    slice1Display.DataAxesGrid.ZTitleFontSize = 12
    slice1Display.DataAxesGrid.ZTitleShadow = 0
    slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
    slice1Display.DataAxesGrid.FacesToRender = 63
    slice1Display.DataAxesGrid.CullBackface = 0
    slice1Display.DataAxesGrid.CullFrontface = 1
    slice1Display.DataAxesGrid.ShowGrid = 0
    slice1Display.DataAxesGrid.ShowEdges = 1
    slice1Display.DataAxesGrid.ShowTicks = 1
    slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    slice1Display.DataAxesGrid.AxesToLabel = 63
    slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.XLabelFontFile = ''
    slice1Display.DataAxesGrid.XLabelBold = 0
    slice1Display.DataAxesGrid.XLabelItalic = 0
    slice1Display.DataAxesGrid.XLabelFontSize = 12
    slice1Display.DataAxesGrid.XLabelShadow = 0
    slice1Display.DataAxesGrid.XLabelOpacity = 1.0
    slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.YLabelFontFile = ''
    slice1Display.DataAxesGrid.YLabelBold = 0
    slice1Display.DataAxesGrid.YLabelItalic = 0
    slice1Display.DataAxesGrid.YLabelFontSize = 12
    slice1Display.DataAxesGrid.YLabelShadow = 0
    slice1Display.DataAxesGrid.YLabelOpacity = 1.0
    slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.ZLabelFontFile = ''
    slice1Display.DataAxesGrid.ZLabelBold = 0
    slice1Display.DataAxesGrid.ZLabelItalic = 0
    slice1Display.DataAxesGrid.ZLabelFontSize = 12
    slice1Display.DataAxesGrid.ZLabelShadow = 0
    slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
    slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.XAxisPrecision = 2
    slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.XAxisLabels = []
    slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.YAxisPrecision = 2
    slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.YAxisLabels = []
    slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.ZAxisPrecision = 2
    slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.ZAxisLabels = []
    slice1Display.DataAxesGrid.UseCustomBounds = 0
    slice1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice1Display.PolarAxes.Visibility = 0
    slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    slice1Display.PolarAxes.EnableCustomRange = 0
    slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
    slice1Display.PolarAxes.PolarAxisVisibility = 1
    slice1Display.PolarAxes.RadialAxesVisibility = 1
    slice1Display.PolarAxes.DrawRadialGridlines = 1
    slice1Display.PolarAxes.PolarArcsVisibility = 1
    slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
    slice1Display.PolarAxes.NumberOfRadialAxes = 0
    slice1Display.PolarAxes.AutoSubdividePolarAxis = 1
    slice1Display.PolarAxes.NumberOfPolarAxis = 0
    slice1Display.PolarAxes.MinimumRadius = 0.0
    slice1Display.PolarAxes.MinimumAngle = 0.0
    slice1Display.PolarAxes.MaximumAngle = 90.0
    slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    slice1Display.PolarAxes.Ratio = 1.0
    slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
    slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    slice1Display.PolarAxes.PolarLabelVisibility = 1
    slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    slice1Display.PolarAxes.RadialLabelVisibility = 1
    slice1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    slice1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    slice1Display.PolarAxes.RadialUnitsVisibility = 1
    slice1Display.PolarAxes.ScreenSize = 10.0
    slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
    slice1Display.PolarAxes.PolarAxisTitleBold = 0
    slice1Display.PolarAxes.PolarAxisTitleItalic = 0
    slice1Display.PolarAxes.PolarAxisTitleShadow = 0
    slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
    slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
    slice1Display.PolarAxes.PolarAxisLabelBold = 0
    slice1Display.PolarAxes.PolarAxisLabelItalic = 0
    slice1Display.PolarAxes.PolarAxisLabelShadow = 0
    slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
    slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    slice1Display.PolarAxes.LastRadialAxisTextBold = 0
    slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
    slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
    slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    slice1Display.PolarAxes.EnableDistanceLOD = 1
    slice1Display.PolarAxes.DistanceLODThreshold = 0.7
    slice1Display.PolarAxes.EnableViewAngleLOD = 1
    slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    slice1Display.PolarAxes.PolarTicksVisibility = 1
    slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    slice1Display.PolarAxes.TickLocation = 'Both'
    slice1Display.PolarAxes.AxisTickVisibility = 1
    slice1Display.PolarAxes.AxisMinorTickVisibility = 0
    slice1Display.PolarAxes.ArcTickVisibility = 1
    slice1Display.PolarAxes.ArcMinorTickVisibility = 0
    slice1Display.PolarAxes.DeltaAngleMajor = 10.0
    slice1Display.PolarAxes.DeltaAngleMinor = 5.0
    slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    slice1Display.PolarAxes.ArcMajorTickSize = 0.0
    slice1Display.PolarAxes.ArcTickRatioSize = 0.3
    slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
    slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
    slice1Display.PolarAxes.Use2DMode = 0
    slice1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(calculator1, renderView1)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=slice1,
        GlyphType='Arrow')
    glyph1.OrientationArray = ['POINTS', 'Result']
    glyph1.ScaleArray = ['POINTS', 'No scale array']
    glyph1.VectorScaleMode = 'Scale by Magnitude'
    glyph1.ScaleFactor = 350.00000000000006
    glyph1.GlyphTransform = 'Transform2'
    glyph1.GlyphMode = 'Uniform Spatial Distribution (Bounds Based)'
    glyph1.MaximumNumberOfSamplePoints = 5000
    glyph1.Seed = 10339
    glyph1.Stride = 1

    # init the 'Arrow' selected for 'GlyphType'
    glyph1.GlyphType.TipResolution = 6
    glyph1.GlyphType.TipRadius = 0.1
    glyph1.GlyphType.TipLength = 0.35
    glyph1.GlyphType.ShaftResolution = 6
    glyph1.GlyphType.ShaftRadius = 0.03
    glyph1.GlyphType.Invert = 0

    # init the 'Transform2' selected for 'GlyphTransform'
    glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]

    # Properties modified on glyph1
    glyph1.OrientationArray = ['POINTS', 'f']
    glyph1.ScaleArray = ['POINTS', 'Result']
    glyph1.ScaleFactor = 7.0
    glyph1.MaximumNumberOfSamplePoints = 800

    # show data in view
    glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    glyph1Display.Selection = None
    glyph1Display.Representation = 'Surface'
    glyph1Display.ColorArrayName = ['POINTS', 'f']
    glyph1Display.LookupTable = fLUT
    glyph1Display.MapScalars = 1
    glyph1Display.MultiComponentsMapping = 0
    glyph1Display.InterpolateScalarsBeforeMapping = 1
    glyph1Display.Opacity = 1.0
    glyph1Display.PointSize = 2.0
    glyph1Display.LineWidth = 1.0
    glyph1Display.RenderLinesAsTubes = 0
    glyph1Display.RenderPointsAsSpheres = 0
    glyph1Display.Interpolation = 'Gouraud'
    glyph1Display.Specular = 0.0
    glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
    glyph1Display.SpecularPower = 100.0
    glyph1Display.Luminosity = 0.0
    glyph1Display.Ambient = 0.0
    glyph1Display.Diffuse = 1.0
    glyph1Display.Roughness = 0.3
    glyph1Display.Metallic = 0.0
    glyph1Display.EdgeTint = [1.0, 1.0, 1.0]
    glyph1Display.Anisotropy = 0.0
    glyph1Display.AnisotropyRotation = 0.0
    glyph1Display.BaseIOR = 1.5
    glyph1Display.CoatStrength = 0.0
    glyph1Display.CoatIOR = 2.0
    glyph1Display.CoatRoughness = 0.0
    glyph1Display.CoatColor = [1.0, 1.0, 1.0]
    glyph1Display.SelectTCoordArray = 'None'
    glyph1Display.SelectNormalArray = 'None'
    glyph1Display.SelectTangentArray = 'None'
    glyph1Display.Texture = None
    glyph1Display.RepeatTextures = 1
    glyph1Display.InterpolateTextures = 0
    glyph1Display.SeamlessU = 0
    glyph1Display.SeamlessV = 0
    glyph1Display.UseMipmapTextures = 0
    glyph1Display.ShowTexturesOnBackface = 1
    glyph1Display.BaseColorTexture = None
    glyph1Display.NormalTexture = None
    glyph1Display.NormalScale = 1.0
    glyph1Display.CoatNormalTexture = None
    glyph1Display.CoatNormalScale = 1.0
    glyph1Display.MaterialTexture = None
    glyph1Display.OcclusionStrength = 1.0
    glyph1Display.AnisotropyTexture = None
    glyph1Display.EmissiveTexture = None
    glyph1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    glyph1Display.FlipTextures = 0
    glyph1Display.BackfaceRepresentation = 'Follow Frontface'
    glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    glyph1Display.BackfaceOpacity = 1.0
    glyph1Display.Position = [0.0, 0.0, 0.0]
    glyph1Display.Scale = [1.0, 1.0, 1.0]
    glyph1Display.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.Origin = [0.0, 0.0, 0.0]
    glyph1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    glyph1Display.Pickable = 1
    glyph1Display.Triangulate = 0
    glyph1Display.UseShaderReplacements = 0
    glyph1Display.ShaderReplacements = ''
    glyph1Display.NonlinearSubdivisionLevel = 1
    glyph1Display.UseDataPartitions = 0
    glyph1Display.OSPRayUseScaleArray = 'All Approximate'
    glyph1Display.OSPRayScaleArray = 'Result'
    glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    glyph1Display.OSPRayMaterial = 'None'
    glyph1Display.BlockSelectors = ['/']
    glyph1Display.BlockColors = []
    glyph1Display.BlockOpacities = []
    glyph1Display.Orient = 0
    glyph1Display.OrientationMode = 'Direction'
    glyph1Display.SelectOrientationVectors = 'Result'
    glyph1Display.Scaling = 0
    glyph1Display.ScaleMode = 'No Data Scaling Off'
    glyph1Display.ScaleFactor = 350.000000000001
    glyph1Display.SelectScaleArray = 'None'
    glyph1Display.GlyphType = 'Arrow'
    glyph1Display.UseGlyphTable = 0
    glyph1Display.GlyphTableIndexArray = 'None'
    glyph1Display.UseCompositeGlyphTable = 0
    glyph1Display.UseGlyphCullingAndLOD = 0
    glyph1Display.LODValues = []
    glyph1Display.ColorByLODIndex = 0
    glyph1Display.GaussianRadius = 17.50000000000005
    glyph1Display.ShaderPreset = 'Sphere'
    glyph1Display.CustomTriangleScale = 3
    glyph1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    glyph1Display.Emissive = 0
    glyph1Display.ScaleByArray = 0
    glyph1Display.SetScaleArray = ['POINTS', 'Result']
    glyph1Display.ScaleArrayComponent = 'X'
    glyph1Display.UseScaleFunction = 1
    glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
    glyph1Display.OpacityByArray = 0
    glyph1Display.OpacityArray = ['POINTS', 'Result']
    glyph1Display.OpacityArrayComponent = 'X'
    glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
    glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
    glyph1Display.SelectionCellLabelBold = 0
    glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    glyph1Display.SelectionCellLabelFontFamily = 'Arial'
    glyph1Display.SelectionCellLabelFontFile = ''
    glyph1Display.SelectionCellLabelFontSize = 18
    glyph1Display.SelectionCellLabelItalic = 0
    glyph1Display.SelectionCellLabelJustification = 'Left'
    glyph1Display.SelectionCellLabelOpacity = 1.0
    glyph1Display.SelectionCellLabelShadow = 0
    glyph1Display.SelectionPointLabelBold = 0
    glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    glyph1Display.SelectionPointLabelFontFamily = 'Arial'
    glyph1Display.SelectionPointLabelFontFile = ''
    glyph1Display.SelectionPointLabelFontSize = 18
    glyph1Display.SelectionPointLabelItalic = 0
    glyph1Display.SelectionPointLabelJustification = 'Left'
    glyph1Display.SelectionPointLabelOpacity = 1.0
    glyph1Display.SelectionPointLabelShadow = 0
    glyph1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    glyph1Display.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
    glyph1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    glyph1Display.GlyphType.TipResolution = 6
    glyph1Display.GlyphType.TipRadius = 0.1
    glyph1Display.GlyphType.TipLength = 0.35
    glyph1Display.GlyphType.ShaftResolution = 6
    glyph1Display.GlyphType.ShaftRadius = 0.03
    glyph1Display.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    glyph1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    glyph1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    glyph1Display.DataAxesGrid.XTitle = 'X Axis'
    glyph1Display.DataAxesGrid.YTitle = 'Y Axis'
    glyph1Display.DataAxesGrid.ZTitle = 'Z Axis'
    glyph1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XTitleFontFile = ''
    glyph1Display.DataAxesGrid.XTitleBold = 0
    glyph1Display.DataAxesGrid.XTitleItalic = 0
    glyph1Display.DataAxesGrid.XTitleFontSize = 12
    glyph1Display.DataAxesGrid.XTitleShadow = 0
    glyph1Display.DataAxesGrid.XTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YTitleFontFile = ''
    glyph1Display.DataAxesGrid.YTitleBold = 0
    glyph1Display.DataAxesGrid.YTitleItalic = 0
    glyph1Display.DataAxesGrid.YTitleFontSize = 12
    glyph1Display.DataAxesGrid.YTitleShadow = 0
    glyph1Display.DataAxesGrid.YTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZTitleFontFile = ''
    glyph1Display.DataAxesGrid.ZTitleBold = 0
    glyph1Display.DataAxesGrid.ZTitleItalic = 0
    glyph1Display.DataAxesGrid.ZTitleFontSize = 12
    glyph1Display.DataAxesGrid.ZTitleShadow = 0
    glyph1Display.DataAxesGrid.ZTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.FacesToRender = 63
    glyph1Display.DataAxesGrid.CullBackface = 0
    glyph1Display.DataAxesGrid.CullFrontface = 1
    glyph1Display.DataAxesGrid.ShowGrid = 0
    glyph1Display.DataAxesGrid.ShowEdges = 1
    glyph1Display.DataAxesGrid.ShowTicks = 1
    glyph1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    glyph1Display.DataAxesGrid.AxesToLabel = 63
    glyph1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XLabelFontFile = ''
    glyph1Display.DataAxesGrid.XLabelBold = 0
    glyph1Display.DataAxesGrid.XLabelItalic = 0
    glyph1Display.DataAxesGrid.XLabelFontSize = 12
    glyph1Display.DataAxesGrid.XLabelShadow = 0
    glyph1Display.DataAxesGrid.XLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YLabelFontFile = ''
    glyph1Display.DataAxesGrid.YLabelBold = 0
    glyph1Display.DataAxesGrid.YLabelItalic = 0
    glyph1Display.DataAxesGrid.YLabelFontSize = 12
    glyph1Display.DataAxesGrid.YLabelShadow = 0
    glyph1Display.DataAxesGrid.YLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZLabelFontFile = ''
    glyph1Display.DataAxesGrid.ZLabelBold = 0
    glyph1Display.DataAxesGrid.ZLabelItalic = 0
    glyph1Display.DataAxesGrid.ZLabelFontSize = 12
    glyph1Display.DataAxesGrid.ZLabelShadow = 0
    glyph1Display.DataAxesGrid.ZLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.XAxisPrecision = 2
    glyph1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.XAxisLabels = []
    glyph1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.YAxisPrecision = 2
    glyph1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.YAxisLabels = []
    glyph1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.ZAxisPrecision = 2
    glyph1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.ZAxisLabels = []
    glyph1Display.DataAxesGrid.UseCustomBounds = 0
    glyph1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    glyph1Display.PolarAxes.Visibility = 0
    glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    glyph1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    glyph1Display.PolarAxes.EnableCustomRange = 0
    glyph1Display.PolarAxes.CustomRange = [0.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisVisibility = 1
    glyph1Display.PolarAxes.RadialAxesVisibility = 1
    glyph1Display.PolarAxes.DrawRadialGridlines = 1
    glyph1Display.PolarAxes.PolarArcsVisibility = 1
    glyph1Display.PolarAxes.DrawPolarArcsGridlines = 1
    glyph1Display.PolarAxes.NumberOfRadialAxes = 0
    glyph1Display.PolarAxes.AutoSubdividePolarAxis = 1
    glyph1Display.PolarAxes.NumberOfPolarAxis = 0
    glyph1Display.PolarAxes.MinimumRadius = 0.0
    glyph1Display.PolarAxes.MinimumAngle = 0.0
    glyph1Display.PolarAxes.MaximumAngle = 90.0
    glyph1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    glyph1Display.PolarAxes.Ratio = 1.0
    glyph1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisTitleVisibility = 1
    glyph1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    glyph1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    glyph1Display.PolarAxes.PolarLabelVisibility = 1
    glyph1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    glyph1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    glyph1Display.PolarAxes.RadialLabelVisibility = 1
    glyph1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    glyph1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    glyph1Display.PolarAxes.RadialUnitsVisibility = 1
    glyph1Display.PolarAxes.ScreenSize = 10.0
    glyph1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
    glyph1Display.PolarAxes.PolarAxisTitleBold = 0
    glyph1Display.PolarAxes.PolarAxisTitleItalic = 0
    glyph1Display.PolarAxes.PolarAxisTitleShadow = 0
    glyph1Display.PolarAxes.PolarAxisTitleFontSize = 12
    glyph1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
    glyph1Display.PolarAxes.PolarAxisLabelBold = 0
    glyph1Display.PolarAxes.PolarAxisLabelItalic = 0
    glyph1Display.PolarAxes.PolarAxisLabelShadow = 0
    glyph1Display.PolarAxes.PolarAxisLabelFontSize = 12
    glyph1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    glyph1Display.PolarAxes.LastRadialAxisTextBold = 0
    glyph1Display.PolarAxes.LastRadialAxisTextItalic = 0
    glyph1Display.PolarAxes.LastRadialAxisTextShadow = 0
    glyph1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    glyph1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    glyph1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    glyph1Display.PolarAxes.EnableDistanceLOD = 1
    glyph1Display.PolarAxes.DistanceLODThreshold = 0.7
    glyph1Display.PolarAxes.EnableViewAngleLOD = 1
    glyph1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    glyph1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    glyph1Display.PolarAxes.PolarTicksVisibility = 1
    glyph1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    glyph1Display.PolarAxes.TickLocation = 'Both'
    glyph1Display.PolarAxes.AxisTickVisibility = 1
    glyph1Display.PolarAxes.AxisMinorTickVisibility = 0
    glyph1Display.PolarAxes.ArcTickVisibility = 1
    glyph1Display.PolarAxes.ArcMinorTickVisibility = 0
    glyph1Display.PolarAxes.DeltaAngleMajor = 10.0
    glyph1Display.PolarAxes.DeltaAngleMinor = 5.0
    glyph1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.ArcMajorTickSize = 0.0
    glyph1Display.PolarAxes.ArcTickRatioSize = 0.3
    glyph1Display.PolarAxes.ArcMajorTickThickness = 1.0
    glyph1Display.PolarAxes.ArcTickRatioThickness = 0.5
    glyph1Display.PolarAxes.Use2DMode = 0
    glyph1Display.PolarAxes.UseLogAxis = 0

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(glyph1Display, ('POINTS', 'Result', 'Magnitude'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(fLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    glyph1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'Result'
    resultLUT = GetColorTransferFunction('Result')

    # get opacity transfer function/opacity map for 'Result'
    resultPWF = GetOpacityTransferFunction('Result')

    # hide data in view
    Hide(slice1, renderView1)

    # reset view to fit data
    renderView1.ResetCamera(False)
  
  if (direction == 'y'):
    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=calculator1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.UseDual = 0
    slice1.Crinkleslice = 0
    slice1.Triangulatetheslice = 1
    slice1.Mergeduplicatedpointsintheslice = 1
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [1000.0000000000001, 1750.0000000000002, 200.00000000000003]
    slice1.SliceType.Normal = [1.0, 0.0, 0.0]
    slice1.SliceType.Offset = 0.0

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [1000.0000000000001, 1750.0000000000002, 200.00000000000003]
    slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]
    slice1.HyperTreeGridSlicer.Offset = 0.0

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [1000.0000000000001, 1450.0, 200.00000000000003]
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'Result'
    resultLUT = GetColorTransferFunction('Result')

    # trace defaults for the display properties.
    slice1Display.Selection = None
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'Result']
    slice1Display.LookupTable = resultLUT
    slice1Display.MapScalars = 1
    slice1Display.MultiComponentsMapping = 0
    slice1Display.InterpolateScalarsBeforeMapping = 1
    slice1Display.Opacity = 1.0
    slice1Display.PointSize = 2.0
    slice1Display.LineWidth = 1.0
    slice1Display.RenderLinesAsTubes = 0
    slice1Display.RenderPointsAsSpheres = 0
    slice1Display.Interpolation = 'Gouraud'
    slice1Display.Specular = 0.0
    slice1Display.SpecularColor = [1.0, 1.0, 1.0]
    slice1Display.SpecularPower = 100.0
    slice1Display.Luminosity = 0.0
    slice1Display.Ambient = 0.0
    slice1Display.Diffuse = 1.0
    slice1Display.Roughness = 0.3
    slice1Display.Metallic = 0.0
    slice1Display.EdgeTint = [1.0, 1.0, 1.0]
    slice1Display.Anisotropy = 0.0
    slice1Display.AnisotropyRotation = 0.0
    slice1Display.BaseIOR = 1.5
    slice1Display.CoatStrength = 0.0
    slice1Display.CoatIOR = 2.0
    slice1Display.CoatRoughness = 0.0
    slice1Display.CoatColor = [1.0, 1.0, 1.0]
    slice1Display.SelectTCoordArray = 'None'
    slice1Display.SelectNormalArray = 'None'
    slice1Display.SelectTangentArray = 'None'
    slice1Display.Texture = None
    slice1Display.RepeatTextures = 1
    slice1Display.InterpolateTextures = 0
    slice1Display.SeamlessU = 0
    slice1Display.SeamlessV = 0
    slice1Display.UseMipmapTextures = 0
    slice1Display.ShowTexturesOnBackface = 1
    slice1Display.BaseColorTexture = None
    slice1Display.NormalTexture = None
    slice1Display.NormalScale = 1.0
    slice1Display.CoatNormalTexture = None
    slice1Display.CoatNormalScale = 1.0
    slice1Display.MaterialTexture = None
    slice1Display.OcclusionStrength = 1.0
    slice1Display.AnisotropyTexture = None
    slice1Display.EmissiveTexture = None
    slice1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    slice1Display.FlipTextures = 0
    slice1Display.BackfaceRepresentation = 'Follow Frontface'
    slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    slice1Display.BackfaceOpacity = 1.0
    slice1Display.Position = [0.0, 0.0, 0.0]
    slice1Display.Scale = [1.0, 1.0, 1.0]
    slice1Display.Orientation = [0.0, 0.0, 0.0]
    slice1Display.Origin = [0.0, 0.0, 0.0]
    slice1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    slice1Display.Pickable = 1
    slice1Display.Triangulate = 0
    slice1Display.UseShaderReplacements = 0
    slice1Display.ShaderReplacements = ''
    slice1Display.NonlinearSubdivisionLevel = 1
    slice1Display.UseDataPartitions = 0
    slice1Display.OSPRayUseScaleArray = 'All Approximate'
    slice1Display.OSPRayScaleArray = 'Result'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.OSPRayMaterial = 'None'
    slice1Display.BlockSelectors = ['/']
    slice1Display.BlockColors = []
    slice1Display.BlockOpacities = []
    slice1Display.Orient = 0
    slice1Display.OrientationMode = 'Direction'
    slice1Display.SelectOrientationVectors = 'Result'
    slice1Display.Scaling = 0
    slice1Display.ScaleMode = 'No Data Scaling Off'
    slice1Display.ScaleFactor = 200.00000000000003
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.UseGlyphTable = 0
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.UseCompositeGlyphTable = 0
    slice1Display.UseGlyphCullingAndLOD = 0
    slice1Display.LODValues = []
    slice1Display.ColorByLODIndex = 0
    slice1Display.GaussianRadius = 10.000000000000002
    slice1Display.ShaderPreset = 'Sphere'
    slice1Display.CustomTriangleScale = 3
    slice1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    slice1Display.Emissive = 0
    slice1Display.ScaleByArray = 0
    slice1Display.SetScaleArray = ['POINTS', 'Result']
    slice1Display.ScaleArrayComponent = 'X'
    slice1Display.UseScaleFunction = 1
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityByArray = 0
    slice1Display.OpacityArray = ['POINTS', 'Result']
    slice1Display.OpacityArrayComponent = 'X'
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.SelectionCellLabelBold = 0
    slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    slice1Display.SelectionCellLabelFontFamily = 'Arial'
    slice1Display.SelectionCellLabelFontFile = ''
    slice1Display.SelectionCellLabelFontSize = 18
    slice1Display.SelectionCellLabelItalic = 0
    slice1Display.SelectionCellLabelJustification = 'Left'
    slice1Display.SelectionCellLabelOpacity = 1.0
    slice1Display.SelectionCellLabelShadow = 0
    slice1Display.SelectionPointLabelBold = 0
    slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    slice1Display.SelectionPointLabelFontFamily = 'Arial'
    slice1Display.SelectionPointLabelFontFile = ''
    slice1Display.SelectionPointLabelFontSize = 18
    slice1Display.SelectionPointLabelItalic = 0
    slice1Display.SelectionPointLabelJustification = 'Left'
    slice1Display.SelectionPointLabelOpacity = 1.0
    slice1Display.SelectionPointLabelShadow = 0
    slice1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    slice1Display.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
    slice1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    slice1Display.GlyphType.TipResolution = 6
    slice1Display.GlyphType.TipRadius = 0.1
    slice1Display.GlyphType.TipLength = 0.35
    slice1Display.GlyphType.ShaftResolution = 6
    slice1Display.GlyphType.ShaftRadius = 0.03
    slice1Display.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [-1.2394185659340529, 0.0, 0.5, 0.0, 20.36701902033715, 1.0, 0.5, 0.0]
    slice1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [-1.2394185659340529, 0.0, 0.5, 0.0, 20.36701902033715, 1.0, 0.5, 0.0]
    slice1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    slice1Display.DataAxesGrid.XTitle = 'X Axis'
    slice1Display.DataAxesGrid.YTitle = 'Y Axis'
    slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
    slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.XTitleFontFile = ''
    slice1Display.DataAxesGrid.XTitleBold = 0
    slice1Display.DataAxesGrid.XTitleItalic = 0
    slice1Display.DataAxesGrid.XTitleFontSize = 12
    slice1Display.DataAxesGrid.XTitleShadow = 0
    slice1Display.DataAxesGrid.XTitleOpacity = 1.0
    slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.YTitleFontFile = ''
    slice1Display.DataAxesGrid.YTitleBold = 0
    slice1Display.DataAxesGrid.YTitleItalic = 0
    slice1Display.DataAxesGrid.YTitleFontSize = 12
    slice1Display.DataAxesGrid.YTitleShadow = 0
    slice1Display.DataAxesGrid.YTitleOpacity = 1.0
    slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    slice1Display.DataAxesGrid.ZTitleFontFile = ''
    slice1Display.DataAxesGrid.ZTitleBold = 0
    slice1Display.DataAxesGrid.ZTitleItalic = 0
    slice1Display.DataAxesGrid.ZTitleFontSize = 12
    slice1Display.DataAxesGrid.ZTitleShadow = 0
    slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
    slice1Display.DataAxesGrid.FacesToRender = 63
    slice1Display.DataAxesGrid.CullBackface = 0
    slice1Display.DataAxesGrid.CullFrontface = 1
    slice1Display.DataAxesGrid.ShowGrid = 0
    slice1Display.DataAxesGrid.ShowEdges = 1
    slice1Display.DataAxesGrid.ShowTicks = 1
    slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    slice1Display.DataAxesGrid.AxesToLabel = 63
    slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.XLabelFontFile = ''
    slice1Display.DataAxesGrid.XLabelBold = 0
    slice1Display.DataAxesGrid.XLabelItalic = 0
    slice1Display.DataAxesGrid.XLabelFontSize = 12
    slice1Display.DataAxesGrid.XLabelShadow = 0
    slice1Display.DataAxesGrid.XLabelOpacity = 1.0
    slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.YLabelFontFile = ''
    slice1Display.DataAxesGrid.YLabelBold = 0
    slice1Display.DataAxesGrid.YLabelItalic = 0
    slice1Display.DataAxesGrid.YLabelFontSize = 12
    slice1Display.DataAxesGrid.YLabelShadow = 0
    slice1Display.DataAxesGrid.YLabelOpacity = 1.0
    slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    slice1Display.DataAxesGrid.ZLabelFontFile = ''
    slice1Display.DataAxesGrid.ZLabelBold = 0
    slice1Display.DataAxesGrid.ZLabelItalic = 0
    slice1Display.DataAxesGrid.ZLabelFontSize = 12
    slice1Display.DataAxesGrid.ZLabelShadow = 0
    slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
    slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.XAxisPrecision = 2
    slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.XAxisLabels = []
    slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.YAxisPrecision = 2
    slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.YAxisLabels = []
    slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    slice1Display.DataAxesGrid.ZAxisPrecision = 2
    slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    slice1Display.DataAxesGrid.ZAxisLabels = []
    slice1Display.DataAxesGrid.UseCustomBounds = 0
    slice1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    slice1Display.PolarAxes.Visibility = 0
    slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    slice1Display.PolarAxes.EnableCustomRange = 0
    slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
    slice1Display.PolarAxes.PolarAxisVisibility = 1
    slice1Display.PolarAxes.RadialAxesVisibility = 1
    slice1Display.PolarAxes.DrawRadialGridlines = 1
    slice1Display.PolarAxes.PolarArcsVisibility = 1
    slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
    slice1Display.PolarAxes.NumberOfRadialAxes = 0
    slice1Display.PolarAxes.AutoSubdividePolarAxis = 1
    slice1Display.PolarAxes.NumberOfPolarAxis = 0
    slice1Display.PolarAxes.MinimumRadius = 0.0
    slice1Display.PolarAxes.MinimumAngle = 0.0
    slice1Display.PolarAxes.MaximumAngle = 90.0
    slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    slice1Display.PolarAxes.Ratio = 1.0
    slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
    slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    slice1Display.PolarAxes.PolarLabelVisibility = 1
    slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    slice1Display.PolarAxes.RadialLabelVisibility = 1
    slice1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    slice1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    slice1Display.PolarAxes.RadialUnitsVisibility = 1
    slice1Display.PolarAxes.ScreenSize = 10.0
    slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
    slice1Display.PolarAxes.PolarAxisTitleBold = 0
    slice1Display.PolarAxes.PolarAxisTitleItalic = 0
    slice1Display.PolarAxes.PolarAxisTitleShadow = 0
    slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
    slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
    slice1Display.PolarAxes.PolarAxisLabelBold = 0
    slice1Display.PolarAxes.PolarAxisLabelItalic = 0
    slice1Display.PolarAxes.PolarAxisLabelShadow = 0
    slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
    slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    slice1Display.PolarAxes.LastRadialAxisTextBold = 0
    slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
    slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
    slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    slice1Display.PolarAxes.EnableDistanceLOD = 1
    slice1Display.PolarAxes.DistanceLODThreshold = 0.7
    slice1Display.PolarAxes.EnableViewAngleLOD = 1
    slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    slice1Display.PolarAxes.PolarTicksVisibility = 1
    slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    slice1Display.PolarAxes.TickLocation = 'Both'
    slice1Display.PolarAxes.AxisTickVisibility = 1
    slice1Display.PolarAxes.AxisMinorTickVisibility = 0
    slice1Display.PolarAxes.ArcTickVisibility = 1
    slice1Display.PolarAxes.ArcMinorTickVisibility = 0
    slice1Display.PolarAxes.DeltaAngleMajor = 10.0
    slice1Display.PolarAxes.DeltaAngleMinor = 5.0
    slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    slice1Display.PolarAxes.ArcMajorTickSize = 0.0
    slice1Display.PolarAxes.ArcTickRatioSize = 0.3
    slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
    slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
    slice1Display.PolarAxes.Use2DMode = 0
    slice1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(calculator1, renderView1)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # find source
    fluxbp = FindSource('flux.bp')

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'Result'
    resultPWF = GetOpacityTransferFunction('Result')

    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=slice1,
        GlyphType='Arrow')
    glyph1.OrientationArray = ['POINTS', 'Result']
    glyph1.ScaleArray = ['POINTS', 'No scale array']
    glyph1.VectorScaleMode = 'Scale by Magnitude'
    glyph1.ScaleFactor = 200.00000000000003
    glyph1.GlyphTransform = 'Transform2'
    glyph1.GlyphMode = 'Uniform Spatial Distribution (Bounds Based)'
    glyph1.MaximumNumberOfSamplePoints = 5000
    glyph1.Seed = 10339
    glyph1.Stride = 1

    # init the 'Arrow' selected for 'GlyphType'
    glyph1.GlyphType.TipResolution = 6
    glyph1.GlyphType.TipRadius = 0.1
    glyph1.GlyphType.TipLength = 0.35
    glyph1.GlyphType.ShaftResolution = 6
    glyph1.GlyphType.ShaftRadius = 0.03
    glyph1.GlyphType.Invert = 0

    # init the 'Transform2' selected for 'GlyphTransform'
    glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]

    # Properties modified on glyph1
    glyph1.OrientationArray = ['POINTS', 'f']
    glyph1.ScaleArray = ['POINTS', 'Result']
    glyph1.ScaleFactor = 6.5
    glyph1.MaximumNumberOfSamplePoints = 400

    # show data in view
    glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    glyph1Display.Selection = None
    glyph1Display.Representation = 'Surface'
    glyph1Display.ColorArrayName = ['POINTS', 'Result']
    glyph1Display.LookupTable = resultLUT
    glyph1Display.MapScalars = 1
    glyph1Display.MultiComponentsMapping = 0
    glyph1Display.InterpolateScalarsBeforeMapping = 1
    glyph1Display.Opacity = 1.0
    glyph1Display.PointSize = 2.0
    glyph1Display.LineWidth = 1.0
    glyph1Display.RenderLinesAsTubes = 0
    glyph1Display.RenderPointsAsSpheres = 0
    glyph1Display.Interpolation = 'Gouraud'
    glyph1Display.Specular = 0.0
    glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
    glyph1Display.SpecularPower = 100.0
    glyph1Display.Luminosity = 0.0
    glyph1Display.Ambient = 0.0
    glyph1Display.Diffuse = 1.0
    glyph1Display.Roughness = 0.3
    glyph1Display.Metallic = 0.0
    glyph1Display.EdgeTint = [1.0, 1.0, 1.0]
    glyph1Display.Anisotropy = 0.0
    glyph1Display.AnisotropyRotation = 0.0
    glyph1Display.BaseIOR = 1.5
    glyph1Display.CoatStrength = 0.0
    glyph1Display.CoatIOR = 2.0
    glyph1Display.CoatRoughness = 0.0
    glyph1Display.CoatColor = [1.0, 1.0, 1.0]
    glyph1Display.SelectTCoordArray = 'None'
    glyph1Display.SelectNormalArray = 'None'
    glyph1Display.SelectTangentArray = 'None'
    glyph1Display.Texture = None
    glyph1Display.RepeatTextures = 1
    glyph1Display.InterpolateTextures = 0
    glyph1Display.SeamlessU = 0
    glyph1Display.SeamlessV = 0
    glyph1Display.UseMipmapTextures = 0
    glyph1Display.ShowTexturesOnBackface = 1
    glyph1Display.BaseColorTexture = None
    glyph1Display.NormalTexture = None
    glyph1Display.NormalScale = 1.0
    glyph1Display.CoatNormalTexture = None
    glyph1Display.CoatNormalScale = 1.0
    glyph1Display.MaterialTexture = None
    glyph1Display.OcclusionStrength = 1.0
    glyph1Display.AnisotropyTexture = None
    glyph1Display.EmissiveTexture = None
    glyph1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    glyph1Display.FlipTextures = 0
    glyph1Display.BackfaceRepresentation = 'Follow Frontface'
    glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    glyph1Display.BackfaceOpacity = 1.0
    glyph1Display.Position = [0.0, 0.0, 0.0]
    glyph1Display.Scale = [1.0, 1.0, 1.0]
    glyph1Display.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.Origin = [0.0, 0.0, 0.0]
    glyph1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    glyph1Display.Pickable = 1
    glyph1Display.Triangulate = 0
    glyph1Display.UseShaderReplacements = 0
    glyph1Display.ShaderReplacements = ''
    glyph1Display.NonlinearSubdivisionLevel = 1
    glyph1Display.UseDataPartitions = 0
    glyph1Display.OSPRayUseScaleArray = 'All Approximate'
    glyph1Display.OSPRayScaleArray = 'Result'
    glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    glyph1Display.OSPRayMaterial = 'None'
    glyph1Display.BlockSelectors = ['/']
    glyph1Display.BlockColors = []
    glyph1Display.BlockOpacities = []
    glyph1Display.Orient = 0
    glyph1Display.OrientationMode = 'Direction'
    glyph1Display.SelectOrientationVectors = 'Result'
    glyph1Display.Scaling = 0
    glyph1Display.ScaleMode = 'No Data Scaling Off'
    glyph1Display.ScaleFactor = 202.1867208480835
    glyph1Display.SelectScaleArray = 'None'
    glyph1Display.GlyphType = 'Arrow'
    glyph1Display.UseGlyphTable = 0
    glyph1Display.GlyphTableIndexArray = 'None'
    glyph1Display.UseCompositeGlyphTable = 0
    glyph1Display.UseGlyphCullingAndLOD = 0
    glyph1Display.LODValues = []
    glyph1Display.ColorByLODIndex = 0
    glyph1Display.GaussianRadius = 10.109336042404175
    glyph1Display.ShaderPreset = 'Sphere'
    glyph1Display.CustomTriangleScale = 3
    glyph1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
      float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
      float gaussian = exp(-0.5*dist2);
      opacity = opacity*gaussian;
    """
    glyph1Display.Emissive = 0
    glyph1Display.ScaleByArray = 0
    glyph1Display.SetScaleArray = ['POINTS', 'Result']
    glyph1Display.ScaleArrayComponent = 'X'
    glyph1Display.UseScaleFunction = 1
    glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
    glyph1Display.OpacityByArray = 0
    glyph1Display.OpacityArray = ['POINTS', 'Result']
    glyph1Display.OpacityArrayComponent = 'X'
    glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
    glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
    glyph1Display.SelectionCellLabelBold = 0
    glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    glyph1Display.SelectionCellLabelFontFamily = 'Arial'
    glyph1Display.SelectionCellLabelFontFile = ''
    glyph1Display.SelectionCellLabelFontSize = 18
    glyph1Display.SelectionCellLabelItalic = 0
    glyph1Display.SelectionCellLabelJustification = 'Left'
    glyph1Display.SelectionCellLabelOpacity = 1.0
    glyph1Display.SelectionCellLabelShadow = 0
    glyph1Display.SelectionPointLabelBold = 0
    glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    glyph1Display.SelectionPointLabelFontFamily = 'Arial'
    glyph1Display.SelectionPointLabelFontFile = ''
    glyph1Display.SelectionPointLabelFontSize = 18
    glyph1Display.SelectionPointLabelItalic = 0
    glyph1Display.SelectionPointLabelJustification = 'Left'
    glyph1Display.SelectionPointLabelOpacity = 1.0
    glyph1Display.SelectionPointLabelShadow = 0
    glyph1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    glyph1Display.OSPRayScaleFunction.Points = [2.1729651585822833e-11, 0.0, 0.5, 0.0, 5.3463965968432026e-05, 1.0, 0.5, 0.0]
    glyph1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    glyph1Display.GlyphType.TipResolution = 6
    glyph1Display.GlyphType.TipRadius = 0.1
    glyph1Display.GlyphType.TipLength = 0.35
    glyph1Display.GlyphType.ShaftResolution = 6
    glyph1Display.GlyphType.ShaftRadius = 0.03
    glyph1Display.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    glyph1Display.ScaleTransferFunction.Points = [-0.15466432247485518, 0.0, 0.5, 0.0, 19.580748091010545, 1.0, 0.5, 0.0]
    glyph1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    glyph1Display.OpacityTransferFunction.Points = [-0.15466432247485518, 0.0, 0.5, 0.0, 19.580748091010545, 1.0, 0.5, 0.0]
    glyph1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    glyph1Display.DataAxesGrid.XTitle = 'X Axis'
    glyph1Display.DataAxesGrid.YTitle = 'Y Axis'
    glyph1Display.DataAxesGrid.ZTitle = 'Z Axis'
    glyph1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XTitleFontFile = ''
    glyph1Display.DataAxesGrid.XTitleBold = 0
    glyph1Display.DataAxesGrid.XTitleItalic = 0
    glyph1Display.DataAxesGrid.XTitleFontSize = 12
    glyph1Display.DataAxesGrid.XTitleShadow = 0
    glyph1Display.DataAxesGrid.XTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YTitleFontFile = ''
    glyph1Display.DataAxesGrid.YTitleBold = 0
    glyph1Display.DataAxesGrid.YTitleItalic = 0
    glyph1Display.DataAxesGrid.YTitleFontSize = 12
    glyph1Display.DataAxesGrid.YTitleShadow = 0
    glyph1Display.DataAxesGrid.YTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZTitleFontFile = ''
    glyph1Display.DataAxesGrid.ZTitleBold = 0
    glyph1Display.DataAxesGrid.ZTitleItalic = 0
    glyph1Display.DataAxesGrid.ZTitleFontSize = 12
    glyph1Display.DataAxesGrid.ZTitleShadow = 0
    glyph1Display.DataAxesGrid.ZTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.FacesToRender = 63
    glyph1Display.DataAxesGrid.CullBackface = 0
    glyph1Display.DataAxesGrid.CullFrontface = 1
    glyph1Display.DataAxesGrid.ShowGrid = 0
    glyph1Display.DataAxesGrid.ShowEdges = 1
    glyph1Display.DataAxesGrid.ShowTicks = 1
    glyph1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    glyph1Display.DataAxesGrid.AxesToLabel = 63
    glyph1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XLabelFontFile = ''
    glyph1Display.DataAxesGrid.XLabelBold = 0
    glyph1Display.DataAxesGrid.XLabelItalic = 0
    glyph1Display.DataAxesGrid.XLabelFontSize = 12
    glyph1Display.DataAxesGrid.XLabelShadow = 0
    glyph1Display.DataAxesGrid.XLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YLabelFontFile = ''
    glyph1Display.DataAxesGrid.YLabelBold = 0
    glyph1Display.DataAxesGrid.YLabelItalic = 0
    glyph1Display.DataAxesGrid.YLabelFontSize = 12
    glyph1Display.DataAxesGrid.YLabelShadow = 0
    glyph1Display.DataAxesGrid.YLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZLabelFontFile = ''
    glyph1Display.DataAxesGrid.ZLabelBold = 0
    glyph1Display.DataAxesGrid.ZLabelItalic = 0
    glyph1Display.DataAxesGrid.ZLabelFontSize = 12
    glyph1Display.DataAxesGrid.ZLabelShadow = 0
    glyph1Display.DataAxesGrid.ZLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.XAxisPrecision = 2
    glyph1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.XAxisLabels = []
    glyph1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.YAxisPrecision = 2
    glyph1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.YAxisLabels = []
    glyph1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.ZAxisPrecision = 2
    glyph1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.ZAxisLabels = []
    glyph1Display.DataAxesGrid.UseCustomBounds = 0
    glyph1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    glyph1Display.PolarAxes.Visibility = 0
    glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    glyph1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    glyph1Display.PolarAxes.EnableCustomRange = 0
    glyph1Display.PolarAxes.CustomRange = [0.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisVisibility = 1
    glyph1Display.PolarAxes.RadialAxesVisibility = 1
    glyph1Display.PolarAxes.DrawRadialGridlines = 1
    glyph1Display.PolarAxes.PolarArcsVisibility = 1
    glyph1Display.PolarAxes.DrawPolarArcsGridlines = 1
    glyph1Display.PolarAxes.NumberOfRadialAxes = 0
    glyph1Display.PolarAxes.AutoSubdividePolarAxis = 1
    glyph1Display.PolarAxes.NumberOfPolarAxis = 0
    glyph1Display.PolarAxes.MinimumRadius = 0.0
    glyph1Display.PolarAxes.MinimumAngle = 0.0
    glyph1Display.PolarAxes.MaximumAngle = 90.0
    glyph1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    glyph1Display.PolarAxes.Ratio = 1.0
    glyph1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisTitleVisibility = 1
    glyph1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    glyph1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    glyph1Display.PolarAxes.PolarLabelVisibility = 1
    glyph1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    glyph1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    glyph1Display.PolarAxes.RadialLabelVisibility = 1
    glyph1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    glyph1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    glyph1Display.PolarAxes.RadialUnitsVisibility = 1
    glyph1Display.PolarAxes.ScreenSize = 10.0
    glyph1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
    glyph1Display.PolarAxes.PolarAxisTitleBold = 0
    glyph1Display.PolarAxes.PolarAxisTitleItalic = 0
    glyph1Display.PolarAxes.PolarAxisTitleShadow = 0
    glyph1Display.PolarAxes.PolarAxisTitleFontSize = 12
    glyph1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
    glyph1Display.PolarAxes.PolarAxisLabelBold = 0
    glyph1Display.PolarAxes.PolarAxisLabelItalic = 0
    glyph1Display.PolarAxes.PolarAxisLabelShadow = 0
    glyph1Display.PolarAxes.PolarAxisLabelFontSize = 12
    glyph1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    glyph1Display.PolarAxes.LastRadialAxisTextBold = 0
    glyph1Display.PolarAxes.LastRadialAxisTextItalic = 0
    glyph1Display.PolarAxes.LastRadialAxisTextShadow = 0
    glyph1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    glyph1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    glyph1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    glyph1Display.PolarAxes.EnableDistanceLOD = 1
    glyph1Display.PolarAxes.DistanceLODThreshold = 0.7
    glyph1Display.PolarAxes.EnableViewAngleLOD = 1
    glyph1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    glyph1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    glyph1Display.PolarAxes.PolarTicksVisibility = 1
    glyph1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    glyph1Display.PolarAxes.TickLocation = 'Both'
    glyph1Display.PolarAxes.AxisTickVisibility = 1
    glyph1Display.PolarAxes.AxisMinorTickVisibility = 0
    glyph1Display.PolarAxes.ArcTickVisibility = 1
    glyph1Display.PolarAxes.ArcMinorTickVisibility = 0
    glyph1Display.PolarAxes.DeltaAngleMajor = 10.0
    glyph1Display.PolarAxes.DeltaAngleMinor = 5.0
    glyph1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.ArcMajorTickSize = 0.0
    glyph1Display.PolarAxes.ArcTickRatioSize = 0.3
    glyph1Display.PolarAxes.ArcMajorTickThickness = 1.0
    glyph1Display.PolarAxes.ArcTickRatioThickness = 0.5
    glyph1Display.PolarAxes.Use2DMode = 0
    glyph1Display.PolarAxes.UseLogAxis = 0

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # hide data in view
    Hide(fluxbp, renderView1)

    # hide data in view
    Hide(slice1, renderView1)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # # update the view to ensure updated data information
    # renderView1.Update()

    # # hide data in view
    # Hide(slice1, renderView1)

  # set active source
  SetActiveSource(slice1)

  # toggle 3D widget visibility (only when running from the GUI)
  Show3DWidgets(proxy=slice1.SliceType)

  # set active source
  SetActiveSource(slice1)

  # show data in view
  slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

  # show color bar/color legend
  slice1Display.SetScalarBarVisibility(renderView1, True)

  # hide data in view
  Hide(slice1, renderView1)

  # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
  resultLUT.ApplyPreset('Viridis (matplotlib)', True)

   # Rescale transfer function
  resultLUT.RescaleTransferFunction(0.0, 3.0e+01)

  # Rescale transfer function
  resultPWF.RescaleTransferFunction(0.0, 3.0e+01)

  # Time steps
  T = parameters["T"]
  num_steps = parameters["num_steps"]
  dt = T/num_steps
  T2 = parameters["T2"]
  num_steps2 = parameters["num_steps2"]
  dt2 = (T2-T)/num_steps2

  if t <= 18:
    # Properties modified on animationScene1
    animationScene1.AnimationTime = t*20*dt
  else:
    # Properties modified on animationScene1
    animationScene1.AnimationTime = T + (t-18)*20*dt2

  # get the time-keeper
  timeKeeper1 = GetTimeKeeper()

  # set active source
  SetActiveSource(calculator1)

  # toggle 3D widget visibility (only when running from the GUI)
  Hide3DWidgets(proxy=slice1.SliceType)

  # get layout
  layout1 = GetLayout()

  # layout/tab size in pixels
  layout1.SetSize(1096, 793)

  if (direction == 'x'):
    # current camera placement for renderView1
    renderView1.CameraPosition = [6347.78858883426, 1750.0, 210.0]
    renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
    renderView1.CameraViewUp = [0.0, -4.440892098500626e-16, -1.0]
    renderView1.CameraParallelScale = 2026.4747716169575
  if (direction == 'y'):
    # current camera placement for renderView1
    renderView1.CameraPosition = [1005.3412954124145, -2569.119649680569, 318.0809373484606]
    renderView1.CameraFocalPoint = [1005.3412954124145, 1450.1468505859375, 318.0809373484606]
    renderView1.CameraViewUp = [-4.440892098500626e-16, 0.0, -1.0]
    renderView1.CameraParallelScale = 1044.5762351384662

  # Make the flux directory
  directory = "flux"
    
  # Parent Directory path
  parent_dir = "../output/plots"
    
  # Path
  path = os.path.join(parent_dir, directory)
  # Check whether the specified path exists or not
  isExist = os.path.exists(path)
  if not isExist:
    # Create the directory
    os.mkdir(path)

  # output file
  t_name = int(t)
  output_filename = f"flux_arrow_{direction}_{t_name}"
  
  # hide data in view
  Hide(slice1, renderView1)

  # save screenshot
  SaveScreenshot(f'../output/plots/flux/{output_filename}.png', renderView1, ImageResolution=[3*1096, 3*793],
      FontScaling='Scale fonts proportionally',
      OverrideColorPalette='',
      StereoMode='No change',
      TransparentBackground=0, 
      # PNG options
      CompressionLevel='5',
      MetaData=['Application', 'ParaView'])
  
  # hide data in view
  Hide(glyph1, renderView1)

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
  renderView1.CameraPosition = [6347.78858883426, 1750.0, 210.0]
  renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
  renderView1.CameraViewUp = [0.0, -4.440892098500626e-16, -1.0]
  renderView1.CameraParallelScale = 2026.4747716169575

  #--------------------------------------------
  # uncomment the following to render all views
  # RenderAllViews()
  # alternatively, if you want to write images, you can use SaveScreenshot(...).
