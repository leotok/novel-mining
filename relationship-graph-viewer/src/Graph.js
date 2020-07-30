import React, { Component } from 'react';
import Graph from "react-graph-vis";
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import axios from 'axios'

// References:
// - https://material-ui.com/
// - https://github.com/crubier/react-graph-vis
// - https://visjs.github.io/vis-network/docs/network/

const BASE_URL = 'http://localhost:8000/graph'

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
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
      nodeSet: new Set(),
      edgeSet: new Set(),
      edges: null,
      network: null,
      currentNode: null,
      defaultPage: 1,
      page: null
    }
  }

  componentDidMount = () => {
    this.fetchGraph(1)
  }

  fetchGraph = (page = null) => {
    if (page === this.state.page) return
    const { nodes, edges, nodeSet, edgeSet } = this.state
    let url = `${BASE_URL}`
    if (page) {
        url = `${url}?page=${page}`
    }

    axios.get(url)
      .then(response => {
        const newNodes = [];
        const newEdges = [];

        for (let nodeIdx in response.data.nodes) {
          const node = response.data.nodes[nodeIdx]
          newNodes.push({ 'id': node.name, 'label': node.name, 'title': node, value: 1, page: node.page, description: node.description })
        }

        this.setState({ 
          edges: response.data.edges,
          nodes: newNodes,
          graph: response.data.graph,
          graphUUID: uuidv4(),
          page: page
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
    const { nodes, edges, defaultPage, page, graphUUID } = this.state
    if (!nodes || !edges) return null

    const graph = { nodes, edges }

    const options = {
      layout: {
        hierarchical: false
      },
      height: "580px",
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
        console.log(obj)
        this.setState({ currentNode: nodes[0] })
      }
    };

    return (
      <div className="row">
        <h1>Relationship Graph Viewer</h1>
        <div>
          <Typography id="page-slider" gutterBottom>
            Page {page}
          </Typography>
          <Slider
            defaultValue={defaultPage}
            onChangeCommitted={this.changePage}
            getAriaValueText={valuetext}
            aria-labelledby="page-slider"
            valueLabelDisplay="auto"
            step={1}
            marks
            min={1}
            max={100}
          />
        </div>
        <div className="col-xs-12">
          <Graph
            key={graphUUID}
            graph={graph}
            options={options}
            events={events}
            getNetwork={network => {
              this.getNetwork(network)
            }}
          />
        </div>
      </div>
    );
  }

}

export default RelationshipGraph;
