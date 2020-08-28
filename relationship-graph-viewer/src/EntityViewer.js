// Author: Leonardo Edelman Wajnsztok
// Date: 07/2020

import React from 'react';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';

const LinkTo = ({to, onClick}) => (
    <Link onClick={onClick} style={{cursor: "pointer"}}>
        {to}
    </Link>
)

export default ({ nodeKey, graph, selectPage, selectEntity }) => {
    const node = graph[nodeKey]
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
                            <p><strong>First appearance on page</strong> <LinkTo to={node.first_page} onClick={() => selectPage(node.first_page)} /></p>
                            <p><strong>Last appearance on page</strong> <LinkTo to={node.last_page} onClick={() => selectPage(node.last_page)} /></p>
                            <p><strong>Appearances: </strong>
                                {node.pages.map((page, i) => (
                                    <span>
                                        {i > 0 && ", "}
                                        <LinkTo to={page} onClick={() => selectPage(page)} />
                                    </span>
                                ))}
                            </p>
                            <p><strong>Relates to: </strong>
                                {node.relations.map((relation, i) => (
                                    <span>
                                        {i > 0 && ", "}
                                        <LinkTo to={graph[relation.to].name} onClick={() => selectEntity(relation.to)} />
                                    </span>
                                ))}
                            </p>
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