import React from 'react';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';


export default ({ node, graph }) => {
    return (
        <Grid
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justify="center"
        >
            <Card style={{ 
                minHeight: 400,
                width: "80%",
                flexDirection:"column",
                display:"flex",
                justifyContent: "center"
            }}>
                <CardContent>
                    {node?
                        <div>
                            <p><strong>Name:</strong> {node.name}</p>
                            {/* <p><strong>Description:</strong> {node.description}</p> */}
                            <p><strong>First appearance on page</strong> {node.first_page}</p>
                            <p><strong>Last appearance on page</strong> {node.last_page}</p>
                            <p><strong>Appearances:</strong> {node.pages.join(', ')}</p>
                            <p><strong>Relates to:</strong> {node.relations.map(r => graph[r.to].name).join(', ')}</p>
                        </div>
                        :
                        <Typography variant="h5" component="h2">
                            Select a node to see its content
                        </Typography>
                    }
                </CardContent>
            </Card>
        </Grid>
    )
}