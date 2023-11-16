from paraview.simple import *
import os
import sys
sys.path.insert(0, "../anderson_junction_subsec5.1")
from default_parameters import parameters

def extract_paraview_AR(input_filepath, t, output_filename):

    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'ADIOS2VTXReader'
    deformationbp = ADIOS2VTXReader(registrationName='deformation.bp', FileName=f'{input_filepath}/deformation.bp')

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    deformationbpDisplay = Show(deformationbp, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    deformationbpDisplay.Selection = None
    deformationbpDisplay.Representation = 'Surface'
    deformationbpDisplay.ColorArrayName = [None, '']
    deformationbpDisplay.LookupTable = None
    deformationbpDisplay.MapScalars = 1
    deformationbpDisplay.MultiComponentsMapping = 0
    deformationbpDisplay.InterpolateScalarsBeforeMapping = 1
    deformationbpDisplay.Opacity = 1.0
    deformationbpDisplay.PointSize = 2.0
    deformationbpDisplay.LineWidth = 1.0
    deformationbpDisplay.RenderLinesAsTubes = 0
    deformationbpDisplay.RenderPointsAsSpheres = 0
    deformationbpDisplay.Interpolation = 'Gouraud'
    deformationbpDisplay.Specular = 0.0
    deformationbpDisplay.SpecularColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.SpecularPower = 100.0
    deformationbpDisplay.Luminosity = 0.0
    deformationbpDisplay.Ambient = 0.0
    deformationbpDisplay.Diffuse = 1.0
    deformationbpDisplay.Roughness = 0.3
    deformationbpDisplay.Metallic = 0.0
    deformationbpDisplay.EdgeTint = [1.0, 1.0, 1.0]
    deformationbpDisplay.Anisotropy = 0.0
    deformationbpDisplay.AnisotropyRotation = 0.0
    deformationbpDisplay.BaseIOR = 1.5
    deformationbpDisplay.CoatStrength = 0.0
    deformationbpDisplay.CoatIOR = 2.0
    deformationbpDisplay.CoatRoughness = 0.0
    deformationbpDisplay.CoatColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.SelectTCoordArray = 'None'
    deformationbpDisplay.SelectNormalArray = 'None'
    deformationbpDisplay.SelectTangentArray = 'None'
    deformationbpDisplay.Texture = None
    deformationbpDisplay.RepeatTextures = 1
    deformationbpDisplay.InterpolateTextures = 0
    deformationbpDisplay.SeamlessU = 0
    deformationbpDisplay.SeamlessV = 0
    deformationbpDisplay.UseMipmapTextures = 0
    deformationbpDisplay.ShowTexturesOnBackface = 1
    deformationbpDisplay.BaseColorTexture = None
    deformationbpDisplay.NormalTexture = None
    deformationbpDisplay.NormalScale = 1.0
    deformationbpDisplay.CoatNormalTexture = None
    deformationbpDisplay.CoatNormalScale = 1.0
    deformationbpDisplay.MaterialTexture = None
    deformationbpDisplay.OcclusionStrength = 1.0
    deformationbpDisplay.AnisotropyTexture = None
    deformationbpDisplay.EmissiveTexture = None
    deformationbpDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
    deformationbpDisplay.FlipTextures = 0
    deformationbpDisplay.BackfaceRepresentation = 'Follow Frontface'
    deformationbpDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.BackfaceOpacity = 1.0
    deformationbpDisplay.Position = [0.0, 0.0, 0.0]
    deformationbpDisplay.Scale = [1.0, 1.0, 1.0]
    deformationbpDisplay.Orientation = [0.0, 0.0, 0.0]
    deformationbpDisplay.Origin = [0.0, 0.0, 0.0]
    deformationbpDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    deformationbpDisplay.Pickable = 1
    deformationbpDisplay.Triangulate = 0
    deformationbpDisplay.UseShaderReplacements = 0
    deformationbpDisplay.ShaderReplacements = ''
    deformationbpDisplay.NonlinearSubdivisionLevel = 1
    deformationbpDisplay.UseDataPartitions = 0
    deformationbpDisplay.OSPRayUseScaleArray = 'All Approximate'
    deformationbpDisplay.OSPRayScaleArray = 'u_n'
    deformationbpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    deformationbpDisplay.OSPRayMaterial = 'None'
    deformationbpDisplay.BlockSelectors = ['/']
    deformationbpDisplay.BlockColors = []
    deformationbpDisplay.BlockOpacities = []
    deformationbpDisplay.Orient = 0
    deformationbpDisplay.OrientationMode = 'Direction'
    deformationbpDisplay.SelectOrientationVectors = 'None'
    deformationbpDisplay.Scaling = 0
    deformationbpDisplay.ScaleMode = 'No Data Scaling Off'
    deformationbpDisplay.ScaleFactor = 350.00000000000006
    deformationbpDisplay.SelectScaleArray = 'None'
    deformationbpDisplay.GlyphType = 'Arrow'
    deformationbpDisplay.UseGlyphTable = 0
    deformationbpDisplay.GlyphTableIndexArray = 'None'
    deformationbpDisplay.UseCompositeGlyphTable = 0
    deformationbpDisplay.UseGlyphCullingAndLOD = 0
    deformationbpDisplay.LODValues = []
    deformationbpDisplay.ColorByLODIndex = 0
    deformationbpDisplay.GaussianRadius = 17.500000000000004
    deformationbpDisplay.ShaderPreset = 'Sphere'
    deformationbpDisplay.CustomTriangleScale = 3
    deformationbpDisplay.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    deformationbpDisplay.Emissive = 0
    deformationbpDisplay.ScaleByArray = 0
    deformationbpDisplay.SetScaleArray = ['POINTS', 'u_n']
    deformationbpDisplay.ScaleArrayComponent = 'X'
    deformationbpDisplay.UseScaleFunction = 1
    deformationbpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    deformationbpDisplay.OpacityByArray = 0
    deformationbpDisplay.OpacityArray = ['POINTS', 'u_n']
    deformationbpDisplay.OpacityArrayComponent = 'X'
    deformationbpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    deformationbpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    deformationbpDisplay.SelectionCellLabelBold = 0
    deformationbpDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    deformationbpDisplay.SelectionCellLabelFontFamily = 'Arial'
    deformationbpDisplay.SelectionCellLabelFontFile = ''
    deformationbpDisplay.SelectionCellLabelFontSize = 18
    deformationbpDisplay.SelectionCellLabelItalic = 0
    deformationbpDisplay.SelectionCellLabelJustification = 'Left'
    deformationbpDisplay.SelectionCellLabelOpacity = 1.0
    deformationbpDisplay.SelectionCellLabelShadow = 0
    deformationbpDisplay.SelectionPointLabelBold = 0
    deformationbpDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    deformationbpDisplay.SelectionPointLabelFontFamily = 'Arial'
    deformationbpDisplay.SelectionPointLabelFontFile = ''
    deformationbpDisplay.SelectionPointLabelFontSize = 18
    deformationbpDisplay.SelectionPointLabelItalic = 0
    deformationbpDisplay.SelectionPointLabelJustification = 'Left'
    deformationbpDisplay.SelectionPointLabelOpacity = 1.0
    deformationbpDisplay.SelectionPointLabelShadow = 0
    deformationbpDisplay.PolarAxes = 'PolarAxesRepresentation'
    deformationbpDisplay.ScalarOpacityFunction = None
    deformationbpDisplay.ScalarOpacityUnitDistance = 59.8130778687876
    deformationbpDisplay.UseSeparateOpacityArray = 0
    deformationbpDisplay.OpacityArrayName = ['POINTS', 'u_n']
    deformationbpDisplay.OpacityComponent = 'X'
    deformationbpDisplay.SelectMapper = 'Projected tetra'
    deformationbpDisplay.SamplingDimensions = [128, 128, 128]
    deformationbpDisplay.UseFloatingPointFrameBuffer = 1

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    deformationbpDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    deformationbpDisplay.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    deformationbpDisplay.GlyphType.TipResolution = 6
    deformationbpDisplay.GlyphType.TipRadius = 0.1
    deformationbpDisplay.GlyphType.TipLength = 0.35
    deformationbpDisplay.GlyphType.ShaftResolution = 6
    deformationbpDisplay.GlyphType.ShaftRadius = 0.03
    deformationbpDisplay.GlyphType.Invert = 0

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    deformationbpDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    deformationbpDisplay.ScaleTransferFunction.UseLogScale = 0

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    deformationbpDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    deformationbpDisplay.OpacityTransferFunction.UseLogScale = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    deformationbpDisplay.DataAxesGrid.XTitle = 'X Axis'
    deformationbpDisplay.DataAxesGrid.YTitle = 'Y Axis'
    deformationbpDisplay.DataAxesGrid.ZTitle = 'Z Axis'
    deformationbpDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.XTitleFontFile = ''
    deformationbpDisplay.DataAxesGrid.XTitleBold = 0
    deformationbpDisplay.DataAxesGrid.XTitleItalic = 0
    deformationbpDisplay.DataAxesGrid.XTitleFontSize = 12
    deformationbpDisplay.DataAxesGrid.XTitleShadow = 0
    deformationbpDisplay.DataAxesGrid.XTitleOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.YTitleFontFile = ''
    deformationbpDisplay.DataAxesGrid.YTitleBold = 0
    deformationbpDisplay.DataAxesGrid.YTitleItalic = 0
    deformationbpDisplay.DataAxesGrid.YTitleFontSize = 12
    deformationbpDisplay.DataAxesGrid.YTitleShadow = 0
    deformationbpDisplay.DataAxesGrid.YTitleOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.ZTitleFontFile = ''
    deformationbpDisplay.DataAxesGrid.ZTitleBold = 0
    deformationbpDisplay.DataAxesGrid.ZTitleItalic = 0
    deformationbpDisplay.DataAxesGrid.ZTitleFontSize = 12
    deformationbpDisplay.DataAxesGrid.ZTitleShadow = 0
    deformationbpDisplay.DataAxesGrid.ZTitleOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.FacesToRender = 63
    deformationbpDisplay.DataAxesGrid.CullBackface = 0
    deformationbpDisplay.DataAxesGrid.CullFrontface = 1
    deformationbpDisplay.DataAxesGrid.ShowGrid = 0
    deformationbpDisplay.DataAxesGrid.ShowEdges = 1
    deformationbpDisplay.DataAxesGrid.ShowTicks = 1
    deformationbpDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
    deformationbpDisplay.DataAxesGrid.AxesToLabel = 63
    deformationbpDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.XLabelFontFile = ''
    deformationbpDisplay.DataAxesGrid.XLabelBold = 0
    deformationbpDisplay.DataAxesGrid.XLabelItalic = 0
    deformationbpDisplay.DataAxesGrid.XLabelFontSize = 12
    deformationbpDisplay.DataAxesGrid.XLabelShadow = 0
    deformationbpDisplay.DataAxesGrid.XLabelOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.YLabelFontFile = ''
    deformationbpDisplay.DataAxesGrid.YLabelBold = 0
    deformationbpDisplay.DataAxesGrid.YLabelItalic = 0
    deformationbpDisplay.DataAxesGrid.YLabelFontSize = 12
    deformationbpDisplay.DataAxesGrid.YLabelShadow = 0
    deformationbpDisplay.DataAxesGrid.YLabelOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
    deformationbpDisplay.DataAxesGrid.ZLabelFontFile = ''
    deformationbpDisplay.DataAxesGrid.ZLabelBold = 0
    deformationbpDisplay.DataAxesGrid.ZLabelItalic = 0
    deformationbpDisplay.DataAxesGrid.ZLabelFontSize = 12
    deformationbpDisplay.DataAxesGrid.ZLabelShadow = 0
    deformationbpDisplay.DataAxesGrid.ZLabelOpacity = 1.0
    deformationbpDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
    deformationbpDisplay.DataAxesGrid.XAxisPrecision = 2
    deformationbpDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
    deformationbpDisplay.DataAxesGrid.XAxisLabels = []
    deformationbpDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
    deformationbpDisplay.DataAxesGrid.YAxisPrecision = 2
    deformationbpDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
    deformationbpDisplay.DataAxesGrid.YAxisLabels = []
    deformationbpDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
    deformationbpDisplay.DataAxesGrid.ZAxisPrecision = 2
    deformationbpDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
    deformationbpDisplay.DataAxesGrid.ZAxisLabels = []
    deformationbpDisplay.DataAxesGrid.UseCustomBounds = 0
    deformationbpDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    deformationbpDisplay.PolarAxes.Visibility = 0
    deformationbpDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
    deformationbpDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    deformationbpDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
    deformationbpDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    deformationbpDisplay.PolarAxes.EnableCustomRange = 0
    deformationbpDisplay.PolarAxes.CustomRange = [0.0, 1.0]
    deformationbpDisplay.PolarAxes.PolarAxisVisibility = 1
    deformationbpDisplay.PolarAxes.RadialAxesVisibility = 1
    deformationbpDisplay.PolarAxes.DrawRadialGridlines = 1
    deformationbpDisplay.PolarAxes.PolarArcsVisibility = 1
    deformationbpDisplay.PolarAxes.DrawPolarArcsGridlines = 1
    deformationbpDisplay.PolarAxes.NumberOfRadialAxes = 0
    deformationbpDisplay.PolarAxes.AutoSubdividePolarAxis = 1
    deformationbpDisplay.PolarAxes.NumberOfPolarAxis = 0
    deformationbpDisplay.PolarAxes.MinimumRadius = 0.0
    deformationbpDisplay.PolarAxes.MinimumAngle = 0.0
    deformationbpDisplay.PolarAxes.MaximumAngle = 90.0
    deformationbpDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
    deformationbpDisplay.PolarAxes.Ratio = 1.0
    deformationbpDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    deformationbpDisplay.PolarAxes.PolarAxisTitleVisibility = 1
    deformationbpDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
    deformationbpDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    deformationbpDisplay.PolarAxes.PolarLabelVisibility = 1
    deformationbpDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
    deformationbpDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
    deformationbpDisplay.PolarAxes.RadialLabelVisibility = 1
    deformationbpDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
    deformationbpDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
    deformationbpDisplay.PolarAxes.RadialUnitsVisibility = 1
    deformationbpDisplay.PolarAxes.ScreenSize = 10.0
    deformationbpDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
    deformationbpDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    deformationbpDisplay.PolarAxes.PolarAxisTitleFontFile = ''
    deformationbpDisplay.PolarAxes.PolarAxisTitleBold = 0
    deformationbpDisplay.PolarAxes.PolarAxisTitleItalic = 0
    deformationbpDisplay.PolarAxes.PolarAxisTitleShadow = 0
    deformationbpDisplay.PolarAxes.PolarAxisTitleFontSize = 12
    deformationbpDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
    deformationbpDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    deformationbpDisplay.PolarAxes.PolarAxisLabelFontFile = ''
    deformationbpDisplay.PolarAxes.PolarAxisLabelBold = 0
    deformationbpDisplay.PolarAxes.PolarAxisLabelItalic = 0
    deformationbpDisplay.PolarAxes.PolarAxisLabelShadow = 0
    deformationbpDisplay.PolarAxes.PolarAxisLabelFontSize = 12
    deformationbpDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
    deformationbpDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    deformationbpDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
    deformationbpDisplay.PolarAxes.LastRadialAxisTextBold = 0
    deformationbpDisplay.PolarAxes.LastRadialAxisTextItalic = 0
    deformationbpDisplay.PolarAxes.LastRadialAxisTextShadow = 0
    deformationbpDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
    deformationbpDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    deformationbpDisplay.PolarAxes.EnableDistanceLOD = 1
    deformationbpDisplay.PolarAxes.DistanceLODThreshold = 0.7
    deformationbpDisplay.PolarAxes.EnableViewAngleLOD = 1
    deformationbpDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
    deformationbpDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
    deformationbpDisplay.PolarAxes.PolarTicksVisibility = 1
    deformationbpDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
    deformationbpDisplay.PolarAxes.TickLocation = 'Both'
    deformationbpDisplay.PolarAxes.AxisTickVisibility = 1
    deformationbpDisplay.PolarAxes.AxisMinorTickVisibility = 0
    deformationbpDisplay.PolarAxes.ArcTickVisibility = 1
    deformationbpDisplay.PolarAxes.ArcMinorTickVisibility = 0
    deformationbpDisplay.PolarAxes.DeltaAngleMajor = 10.0
    deformationbpDisplay.PolarAxes.DeltaAngleMinor = 5.0
    deformationbpDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
    deformationbpDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
    deformationbpDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
    deformationbpDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
    deformationbpDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    deformationbpDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    deformationbpDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    deformationbpDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    deformationbpDisplay.PolarAxes.ArcMajorTickSize = 0.0
    deformationbpDisplay.PolarAxes.ArcTickRatioSize = 0.3
    deformationbpDisplay.PolarAxes.ArcMajorTickThickness = 1.0
    deformationbpDisplay.PolarAxes.ArcTickRatioThickness = 0.5
    deformationbpDisplay.PolarAxes.Use2DMode = 0
    deformationbpDisplay.PolarAxes.UseLogAxis = 0

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(deformationbpDisplay, ('POINTS', 'u_n', 'Magnitude'))

    # rescale color and/or opacity maps used to include current data range
    deformationbpDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    deformationbpDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'u_n'
    u_nLUT = GetColorTransferFunction('u_n')

    # get opacity transfer function/opacity map for 'u_n'
    u_nPWF = GetOpacityTransferFunction('u_n')

    # Rescale transfer function
    u_nLUT.RescaleTransferFunction(0.0, 0.003)

    # Rescale transfer function
    u_nPWF.RescaleTransferFunction(0.0, 0.003)

    # Time steps
    T = parameters["T"]
    num_steps = parameters["num_steps"]
    dt = T/num_steps

    # Properties modified on animationScene1
    animationScene1.AnimationTime = t*20*dt

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    u_nLUT.ApplyPreset('Viridis (matplotlib)', True)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(1096, 793)

    # current camera placement for renderView1
    renderView1.CameraPosition = [1000.0, 1750.0, -7619.697272912243]
    renderView1.CameraFocalPoint = [1000.0, 1750.0, 210.0]
    renderView1.CameraViewUp = [0.5877852522924731, 0.8090169943749475, 0.0]
    renderView1.CameraParallelScale = 2026.4747716169575

    # Check whether the specified output directory exists or not
    isExist = os.path.exists("../output/plots/Anisotropy_ratio")
    if not isExist:
        # Create the directory
        os.mkdir("../output/plots/Anisotropy_ratio")

    # save screenshot
    SaveScreenshot(f'../output/plots/Anisotropy_ratio/{output_filename}.png', renderView1, ImageResolution=[3*1096, 3*793],
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
