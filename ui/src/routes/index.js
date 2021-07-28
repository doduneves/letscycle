import React from "react";
import {
  Table,
  Container,
  Jumbotron,
  Nav
} from 'react-bootstrap'

import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function Routes() {
  const { data, error } = useSWR('/public/routes/', fetcher)

  if (!data || error) {
    return <p>Loading...</p>
  }

  return (
    <>
      <Container>
        <Jumbotron>
          <h1 className="display-3">Lets Cycle</h1>
          <p className="lead">
            An app for cycling and having fun :)
          </p>
        </Jumbotron>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Route Name</th>
              <th>Level</th>
              <th>Avg Rating</th>
            </tr>
          </thead>
          <tbody>
            {data.map((route, index) => {
              return (
                <tr key={index}>
                  <td><Nav.Link href={`/edit/${route.id}`}>{route.name}</Nav.Link></td>
                  <td>{route.level}</td>
                  <td>{route.average_rating}</td>
                </tr>
              )
            })}
          </tbody>
        </Table>
      </Container>
    </>
  )
}