import React from 'react';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import RelationshipGraph from './Graph';
import './App.css';

function App() {
  return (
    <div className="App">
      <Container maxWidth="sm">
        <Box my={4}>
          <RelationshipGraph />
        </Box>
      </Container>
    </div>
  );
}

export default App;
