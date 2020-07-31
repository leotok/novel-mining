import React from 'react';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';


export default ({ node }) => {
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
                            <p>Name: {node.name}</p>
                            <p>Description: {node.description}</p>
                            <p>First appearance on page {node.page}</p>
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