import React, { useState, useEffect } from "react";
import { Button, Col, Container, Form, Jumbotron, Nav, Row } from 'react-bootstrap'
import { MapContainer, TileLayer, Polyline } from 'react-leaflet'
import { useParams } from "react-router-dom";
import Moment from 'moment'

import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function EditRoute() {
    const { id } = useParams();
    const { data, error } = useSWR('/public/routes/' + id, fetcher)

    const [route, setRoute] = useState({})
    const [coordinates, setCoordinates] = useState([])

    useEffect(() => {
        setRoute({
            name: data ? data.name : '',
            level: data ? data.level : '',
            average_rating: data ? data.average_rating : '',
            created_at: data ? Moment(data.created_at).format('MM/DD/YYYY') : '',
            creator: data ? data.creator : '',
            coordinates: data ? data.coordinates : [],
        })

        if(data){
            const latlong = data.coordinates.map((coord, _index) => {
                return [coord.latitude, coord.longitude]
            })

            setCoordinates(latlong)
        }

    }, [data])


    if (!data || error) {
        return <p>Loading...</p>
    }

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setRoute((prevState) => ({
            ...prevState,
            [name]: value
          }));
    }

    console.log(route)
    console.log(coordinates[0])

    const handleOnSubmit = (event) => {
    }

    return (
        <>
        <Container>
            <Jumbotron>
            <h1>Route</h1>
            <div className="main-form">
                <Row>
                <Col xs={6}>
                    <h3>General Informations</h3>
                    <Form onSubmit={handleOnSubmit}>
                        <Form.Group controlId="name">
                            <Form.Label>Name</Form.Label>
                            <Form.Control
                                className="input-control"
                                type="text"
                                name="name"
                                value={route.name}
                                placeholder="Enter a name for the route"
                                onChange={handleInputChange}
                            />
                        </Form.Group>
                        <Form.Group controlId="level">
                            <Form.Label>Level</Form.Label>
                            <Form.Control
                                as="select"
                                name="level"
                                aria-label="Select the route level"
                                defaultValue={route.level}
                                onChange={handleInputChange}
                            >
                                <option>Select the route level</option>
                                <option value="1">Beginner</option>
                                <option value="2">Regular</option>
                                <option value="3">Advance</option>
                            </Form.Control>
                        </Form.Group>
                        <Form.Group controlId="quantity">
                            <Form.Label>Created At</Form.Label>
                            <Form.Control
                                disabled
                                className="input-control"
                                type="text"
                                name="create_at"
                                defaultValue={route.created_at}
                            />
                        </Form.Group>
                        <Form.Group controlId="price">
                            <Form.Label>Created By</Form.Label>
                            <Form.Control
                                disabled
                                className="input-control"
                                type="text"
                                name="creator_name"
                                defaultValue={route.creator}
                            />
                        </Form.Group>
                        <Button
                            variant="primary"
                            type="submit"
                            className="submit-btn"
                            disabled
                        >
                        Submit
                        </Button>
                        <Nav.Link href="/">Back</Nav.Link>
                    </Form>
                </Col>
                <Col xs={6}>
                    <h2>Map</h2>
                    {
                    (coordinates.length > 0) ?
                    <MapContainer center={coordinates[0]} zoom={13} scrollWheelZoom={true}>
                        <TileLayer
                            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />

                        <Polyline pathOptions={{color: '#f67'}} positions={coordinates} />
                    </MapContainer> :
                    <span>No coordinates on this route</span>
                    }
                </Col>
                </Row>


                </div>
            </Jumbotron>

        </Container>
        </>
    )
}