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

const MOCK_DATA = false
const BASE_URL = `http://localhost:8000/graph?mock=${(MOCK_DATA)? 1 : 0}`

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
      defaultPage: null,
      page: null,
      maxPage: null,
      bookName: '',
    }
  }

  componentDidMount = () => {
    this.fetchGraph(9) // TODO: correct first page
  }

  fetchGraph = (page = null) => {
    if (page === this.state.page) return
    let url = `${BASE_URL}`
    if (page) {
        url = `${url}&page=${page}`
    }

    axios.get(url)
      .then(response => {
        const newNodes = [];

        for (let nodeIdx in response.data.nodes) {
          const node = response.data.nodes[nodeIdx]
          newNodes.push({
            id: node.id,
            label: node.name,
            title: node.name,
            value: node.pages.length,
            description: node.description,
            firstPage: node.first_page,
            lastPage: node.last_page,
            pages: node.pages,
          })
        }

        this.setState({
          edges: response.data.edges,
          nodes: newNodes,
          graph: response.data.graph,
          graphUUID: uuidv4(),
          page: page,
          maxPage: response.data.max_page,
          firstPage: response.data.first_page,
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

  selectEntity = (name) => {
    this.setState({ currentNode: name })
    console.log(name)
  }

  render() {
    const { nodes, edges, page, graphUUID, currentNode, graph, maxPage, firstPage, bookName } = this.state
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
          maximum: 200
        },
        scaling: {
          min: 80,
          max: 200,
          label: false,
          // customScalingFunction: (min,max,total,value)=> {
          //     var scale = 1 / (max - min);
          //     return Math.max(0,(value - min)*scale);
          // }
        }
      },
      edges: {
        arrows: {
          to: {
            enabled: false
          }
        },
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

        <Typography style={{marginBottom: 30}} variant='h5'>Graph with {nodes.length} entities until page {page}</Typography>

          <Slider
            marks={ [{value: firstPage, label: `Page ${firstPage}`}, {value: maxPage, label: `Page ${maxPage}`}] }
            defaultValue={firstPage}
            onChangeCommitted={this.changePage}
            getAriaValueText={valuetext}
            aria-labelledby="page-slider"
            valueLabelDisplay="auto"
            step={1}
            min={firstPage}
            max={maxPage}
            value={page}
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
            <Typography variant='h5'style={{ marginBottom: 60 }} >Entity</Typography>
            <EntityViewer
              nodeKey={currentNode}
              graph={graph}
              selectPage={this.fetchGraph}
              selectEntity={this.selectEntity}
            />
          </Box>
        </Grid>
      </Grid>
    );
  }

}

export default RelationshipGraph;
