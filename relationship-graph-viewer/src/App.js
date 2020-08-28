// Author: Leonardo Edelman Wajnsztok
// Date: 07/2020

import React from 'react';
import Container from '@material-ui/core/Container';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import RelationshipGraph from './Graph';
import './App.css';

function App() {
  return (
    <div className="App">
      <AppBar position="static" style={{ backgroundColor: '#1976d2', marginBottom: 30 }}>
        <Toolbar style={{
                    float       : 'none',
                    marginLeft  : 'auto',
                    marginRight : 'auto',
                }}>
          <Typography variant="h5" >
            <Box fontWeight="fontWeightBold">
              Relationship Graph Viewer
            </Box>
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg">
        <RelationshipGraph />
      </Container>
    </div>
  );
}

export default App;
