import React from "react";
import { Table, Container, Jumbotron } from 'reactstrap'

import useSWR from 'swr'

export default function Geopressures() {
  const { data, error } = useSWR('http://localhost:8044/public/routes/')

  console.log(data)


  return (
    <>
      <Container>
        <Jumbotron>
          <h1 className="display-3">Lets Cycle</h1>
          <p className="lead">
            An app for cycle and having fun :)
          </p>
        </Jumbotron>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Route Name</th>
              <th>Level</th>
            </tr>
          </thead>
          <tbody></tbody>
        </Table>
      </Container>
    </>
  )
}