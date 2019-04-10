import _plotly_utils.basevalidators


class SpikesidesValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='spikesides',
        parent_name='layout.scene.yaxis',
        **kwargs
    ):
        super(SpikesidesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )