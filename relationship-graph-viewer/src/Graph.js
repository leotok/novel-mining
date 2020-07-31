import React, { Component } from 'react';
import Graph from "react-graph-vis";
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import axios from 'axios'
import EntityViewer from './EntityViewer'
import { Box } from '@material-ui/core';

// References:
// - https://material-ui.com/
// - https://github.com/crubier/react-graph-vis
// - https://visjs.github.io/vis-network/docs/network/

const BASE_URL = 'http://localhost:8000/graph'

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

function valuetext(value) {
  return `Page ${value}`;
}


class RelationshipGraph extends Component {

  constructor(props) {
    super(props)
    
    this.state = {
      graph: null,
      graphUUID: null,
      nodes: null,
      edges: null,
      network: null,
      currentNode: null,
      defaultPage: 1,
      page: null,
      maxPage: null,
      bookName: '',
    }
  }

  componentDidMount = () => {
    this.fetchGraph(1)
  }

  fetchGraph = (page = null) => {
    if (page === this.state.page) return
    let url = `${BASE_URL}`
    if (page) {
        url = `${url}?page=${page}`
    }

    axios.get(url)
      .then(response => {
        const newNodes = [];

        for (let nodeIdx in response.data.nodes) {
          const node = response.data.nodes[nodeIdx]
          newNodes.push({ 'id': node.name, 'label': node.name, 'title': node, value: 1, page: node.page, description: node.description })
        }

        this.setState({ 
          edges: response.data.edges,
          nodes: newNodes,
          graph: response.data.graph,
          graphUUID: uuidv4(),
          page: page,
          maxPage: response.data.max_page,
          bookName: response.data.book_name,
        })
      })
      .catch(error => {
        if (error.response) {
          console.log(error)
        }
      })
  }

  getNetwork = (network) => {
    this.network = network
  }

  changePage = (event, page) => {
    this.fetchGraph(page)
  }

  render() {
    const { nodes, edges, defaultPage, page, graphUUID, currentNode, graph, maxPage, bookName } = this.state
    if (!nodes || !edges) return null

    const options = {
      layout: {
        hierarchical: false
      },
      height: "500px",
      nodes: {
        shape: 'circle',
        widthConstraint: {
          minimum: 80,
          maximum: 150
        },
        scaling: {
          min: 80,
          max: 150,
          label: false,
          customScalingFunction: (min,max,total,value)=> {
              var scale = 1 / (max - min);
              return Math.max(0,(value - min)*scale);
          }
        }
      },
      edges: {
        smooth: {
          forceDirection: "none"
        }
      },
      physics: {
        forceAtlas2Based: {
          springLength: 130
        },
        minVelocity: 0.88,
        solver: "forceAtlas2Based"
      }
    };
  
    const events = {
      click: (obj) => {
        var { nodes, edges, event, pointer, items } = obj;
        this.setState({ currentNode: nodes[0] })
      }
    };

    return (
      <Grid container>
        <Grid style={{ marginBottom: 30 }} item xs={12}>
          <Typography variant='h5'>
            Book "{bookName}"
          </Typography>
        </Grid>
        <Grid item xs={6}>

          <Typography variant='h6'>Graph at page {page}</Typography>
          
          <Slider
            marks={ [{value: 1, label: 'Page 1'}, {value: maxPage, label: `Page ${maxPage}`}] }
            defaultValue={defaultPage}
            onChangeCommitted={this.changePage}
            getAriaValueText={valuetext}
            aria-labelledby="page-slider"
            valueLabelDisplay="auto"
            step={1}
            min={1}
            max={maxPage}
          />

          <Graph
            key={graphUUID}
            graph={{ nodes, edges }}
            options={options}
            events={events}
            getNetwork={network => {
              this.getNetwork(network)
            }}
          />

        </Grid>
        
        <Grid item xs={6}>
          <Box centered >
            <Typography variant='h6'style={{ marginBottom: 60 }} >Entity</Typography>
            <EntityViewer node={graph[currentNode]}/>
          </Box>
        </Grid>
      </Grid>
    );
  }

}

export default RelationshipGraph;
