# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:13:43 2022

@author: Mario
"""
from flask import Flask, jsonify, request
from models import Models as model


app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not found page</h1>", 404

# GET ALL


@app.route('/get_points', methods=['GET'])
def get_points():
    try:
        points = model.Model.get_points()
        if points is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return points
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_lines', methods=['GET'])
def get_lines():
    try:
        lines = model.Model.get_lines()
        if lines is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return lines
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_circunferences', methods=['GET'])
def get_circunferences():
    try:
        circunferences = model.Model.get_circunferences()
        if circunferences is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return circunferences
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elipses', methods=['GET'])
def get_elipses():
    try:
        elipses = model.Model.get_elipses()
        if elipses is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return elipses
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_hiperbolas', methods=['GET'])
def get_hiperbolas():
    try:
        hiperbolas = model.Model.get_hiperbolas()
        if hiperbolas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return hiperbolas
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_parabolas', methods=['GET'])
def get_parabolas():
    try:
        parabolas = model.Model.get_parabolas()
        if parabolas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return parabolas
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# GET BY ID

@app.route('/get_point_byid/<id_punto>', methods=['GET'])
def get_point_byid(id_punto):
    try:
        point = model.Model.get_point_byid(id_punto)
        if point is None:
            return jsonify({'message': 'Point not found!'}), 404
        else:
            return point
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_line_byid/<id_recta>', methods=['GET'])
def get_line_byid(id_recta):
    try:
        line = model.Model.get_line_byid(id_recta)
        if line is None:
            return jsonify({'message': 'Line not found!'}), 404
        else:
            return line[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_circunference_byid/<id_circunference>', methods=['GET'])
def get_circunference_byid(id_circunference):
    try:
        circunference = model.Model.get_circunference_byid(id_circunference)
        if circunference is None:
            return jsonify({'message': 'Circunference not found!'}), 404
        else:
            return circunference[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elipse_byid/<id_elipse>', methods=['GET'])
def get_elipse_byid(id_elipse):
    try:
        elipse = model.Model.get_elipse_byid(id_elipse)
        if elipse is None:
            return jsonify({'message': 'Elipse not found!'}), 404
        else:
            return elipse[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_hiperbola_byid/<id_hiperbola>', methods=['GET'])
def get_hiperbola_byid(id_hiperbola):
    try:
        hiperbola = model.Model.get_hiperbola_byid(id_hiperbola)
        if hiperbola is None:
            return jsonify({'message': 'Hiperbola not found!'}), 404
        else:
            return hiperbola[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_parabola_byid/<id_parabola>', methods=['GET'])
def get_parabola_byid(id_parabola):
    try:
        parabola = model.Model.get_parabola_byid(id_parabola)
        if parabola is None:
            return jsonify({'message': 'Line not found!'}), 404
        else:
            return parabola[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_point', methods=['POST'])
def create_point():
    try:
        data = request.json
        point = model.Model.create_point(data)
        if point is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Point inserted successfully!',
                'point': point
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_line', methods=['POST'])
def create_line():
    try:
        data = request.json
        line = model.Model.create_line(data)
        if line is None:
            return jsonify({'message': 'Insert line failed!'}), 404
        else:
            return jsonify({
                'message': 'Line inserted successfully!',
                'line': line
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_circunference', methods=['POST'])
def create_circunference():
    try:
        data = request.json
        circunference = model.Model.create_circunference(data)
        if circunference is None:
            return jsonify({'message': 'Insert circunference failed!'}), 404
        else:
            return jsonify({
                'message': 'Circunference inserted successfully!',
                'circunference': circunference
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_parabola', methods=['POST'])
def create_parabola():
    try:
        data = request.json
        parabola = model.Model.create_parabola(data)
        if parabola is None:
            return jsonify({'message': 'Insert parabola failed!'}), 404
        else:
            return jsonify({
                'message': 'Parabola inserted successfully!',
                'parabola': parabola
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_elipse', methods=['POST'])
def create_elipse():
    try:
        data = request.json
        elipse = model.Model.create_elipse(data)
        if elipse is None:
            return jsonify({'message': 'Insert elipse failed!'}), 404
        else:
            return jsonify({
                'message': 'Elipse inserted successfully!',
                'elipse': elipse
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/create_hiperbola', methods=['POST'])
def create_hiperbola():
    try:
        data = request.json
        hiperbola = model.Model.create_hiperbola(data)
        if hiperbola is None:
            return jsonify({'message': 'Insert hiperbola failed!'}), 404
        else:
            return jsonify({
                'message': 'Hiperbola inserted successfully!',
                'hiperbola': hiperbola
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_point/<id_punto>', methods=['PUT'])
def update_point(id_punto):
    try:
        data = request.json
        point = model.Model.update_point(id_punto, data)
        if point is None:
            return jsonify({'message': 'Point updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Point updated successfully!',
                'point': point.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_line/<id_line>', methods=['PUT'])
def update_line(id_line):
    try:
        data = request.json
        line = model.Model.update_line(id_line, data)
        if line is None:
            return jsonify({'message': 'Update line failed, Line not found!'}), 404
        else:
            return jsonify({
                'message': 'Line updated successfully!',
                'line': line.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_circunference/<id_circunference>', methods=['PUT'])
def update_circunference(id_circunference):
    try:
        data = request.json
        circunference = model.Model.update_circunference(
            id_circunference, data)
        if circunference is None:
            return jsonify({'message': 'Update circunference failed, circunference not found!'}), 404
        else:
            return jsonify({
                'message': 'Circunference updated successfully!',
                'circunference': circunference.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_parabola/<id_parabola>', methods=['PUT'])
def update_parabola(id_parabola):
    try:
        data = request.json
        parabola = model.Model.update_parabola(id_parabola, data)
        if parabola is None:
            return jsonify({'message': 'Update parabola failed, parabola not found!'}), 404
        else:
            return jsonify({
                'message': 'Parabola updated successfully!',
                'parabola': parabola.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_elipse/<id_elipse>', methods=['PUT'])
def update_elipse(id_elipse):
    try:
        data = request.json
        elipse = model.Model.update_elipse(id_elipse, data)
        if elipse is None:
            return jsonify({'message': 'Update elipse failed, elipse not found!'}), 404
        else:
            return jsonify({
                'message': 'Elipse updated successfully!',
                'elipse': elipse.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/update_hiperbola/<id_hiperbola>', methods=['PUT'])
def update_hiperbola(id_hiperbola):
    try:
        data = request.json
        hiperbola = model.Model.update_hiperbola(id_hiperbola, data)
        if hiperbola is None:
            return jsonify({'message': 'Update hiperbola failed, hiperbola not found!'}), 404
        else:
            return jsonify({
                'message': 'Hiperbola updated successfully!',
                'hiperbola': hiperbola.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_point/<id_punto>', methods=['DELETE'])
def delete_point(id_punto):
    try:
        row_affect = model.Model.delete_point(id_punto)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_line/<id_line>', methods=['DELETE'])
def delete_line(id_line):
    try:
        row_affect = model.Model.delete_line(id_line)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_circunference/<id_circunference>', methods=['DELETE'])
def delete_circunference(id_circunference):
    try:
        row_affect = model.Model.delete_circunference(id_circunference)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_parabola/<id_parabola>', methods=['DELETE'])
def delete_parabola(id_parabola):
    try:
        row_affect = model.Model.delete_parabola(id_parabola)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_elipse/<id_elipse>', methods=['DELETE'])
def delete_elipse(id_elipse):
    try:
        row_affect = model.Model.delete_elipse(id_elipse)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/delete_hiperbola/<id_hiperbola>', methods=['DELETE'])
def delete_hiperbola(id_hiperbola):
    try:
        row_affect = model.Model.delete_hiperbola(id_hiperbola)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_linebyid/<id_line>', methods=['GET'])
def get_elements_linebyid(id_line):
    try:
        line = model.Model.get_elements_line_byid(id_line)
        if line is None:
            return jsonify({'message': 'Line not found!'})
        else:
            return line.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_circunferencebyid/<id_circunference>', methods=['GET'])
def get_elements_circunferencebyid(id_circunference):
    try:
        circunference = model.Model.get_elements_circunference_byid(
            id_circunference)
        if circunference is None:
            return jsonify({'message': 'Circunference not found!'})
        else:
            return circunference.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_parabolabyid/<id_parabola>', methods=['GET'])
def get_elements_parabolabyid(id_parabola):
    try:
        parabola = model.Model.get_elements_parabola_byid(id_parabola)
        if parabola is None:
            return jsonify({'message': 'Parabola not found!'})
        else:
            return parabola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_elipsebyid/<id_elipse>', methods=['GET'])
def get_elements_elipsebyid(id_elipse):
    try:
        elipse = model.Model.get_elements_elipse_byid(id_elipse)
        if elipse is None:
            return jsonify({'message': 'Elipse not found!'})
        else:
            return elipse.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_hiperbolabyid/<id_hiperbola>', methods=['GET'])
def get_elements_hiperbolabyid(id_hiperbola):
    try:
        hiperbola = model.Model.get_elements_hiperbola_byid(id_hiperbola)
        if hiperbola is None:
            return jsonify({'message': 'Hiperbola not found!'})
        else:
            return hiperbola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_line', methods=['GET'])
def get_elements_line():
    try:
        data = request.json
        line = model.Model.get_elements_line(data)
        if line is None:
            return jsonify({'message': 'Data Line not found!'})
        else:
            return line.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_circunference', methods=['GET'])
def get_elements_circunference():
    try:
        data = request.json
        circunference = model.Model.get_elements_circunference(data)
        if circunference is None:
            return jsonify({'message': 'Data Circunference not found!'})
        else:
            return circunference.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_parabola', methods=['GET'])
def get_elements_parabola():
    try:
        data = request.json
        parabola = model.Model.get_elements_parabola(data)
        if parabola is None:
            return jsonify({'message': 'Data Parabola not found!'})
        else:
            return parabola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_elipse', methods=['GET'])
def get_elements_elipse():
    try:
        data = request.json
        elipse = model.Model.get_elements_elipse(data)
        if elipse is None:
            return jsonify({'message': 'Data Elipse not found!'})
        else:
            return elipse.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/get_elements_hiperbola', methods=['GET'])
def get_elements_hiperbola():
    try:
        data = request.json
        hiperbola = model.Model.get_elements_hiperbola(data)
        if hiperbola is None:
            return jsonify({'message': 'Data Hiperbola not found!'})
        else:
            return hiperbola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/jpg" href="https://www.shutterstock.com/image-vector/realistic-full-moon-detailed-vector-260nw-439390066.jpg">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Poppins:wght@300;400;500;600;700;800&display=swap");
:root {
  --color-primary: #7380ec;
  --color-danger: #ff7782;
  --color-success: #41f1b6;
  --color-warning: #ffbb55;
  --color-white: #fff;
  --color-info-dark: #7d8da1;
  --color-info-light: #dce1eb;
  --color-dark: #363949;
  --color-light: rgba(132, 139, 200, 0.18);
  --color-primary-variant: #111e88;
  --color-dark-variant: #677483;
  --color-background: #f6f6f9;
  --color-gardient-variant: linear-gradient(to right, red 0%, blue 100%);

  --card-border-radius: 2rem;
  --border-radius-1: 0.4rem;
  --border-radius-2: 0.8rem;
  --border-radius-3: 1.2rem;

  --card-padding: 1.8rem;
  --padding: 1.2rem;

  --box-shadow: 0 2rem 3rem var(--color-light);
}

.dark-theme-variables {
  --color-background: #181a1e;
  --color-white: #202528;
  --color-dark: #edeffd;
  --color-dark-variant: #a3bdcc;
  --color-light: rgba(0, 0, 0, 0.4);
  --box-shadow: 0 2rem 3rem var(--color-light);
}

* {
  margin: 0;
  padding: 0;
  outline: 0;
  appearance: none;
  border: 0;
  text-decoration: none;
  list-style: none;
  box-sizing: border-box;
}

html {
  font-size: 14px;
}

body {
  width: 100vw;
  height: 100vh;
  font-family: poppins, sans-serif;
  font-size: 0.88rem;
  background: var(--color-background);
  user-select: none;
  overflow-x: hidden;
  color: var(--color-dark);
}

.container {
  display: grid;
  width: 96%;
  margin: 0 auto;
  gap: 1.8rem;
  grid-template-columns: 14rem auto 23rem;
}

a {
  color: var(--color-dark);
}

img {
  display: block;
  width: 100%;
}

h1 {
  font-weight: 800;
  font-size: 1.8rem;
}
h2 {
  font-size: 1.4rem;
}

h3 {
  font-size: 0.87rem;
}

h4 {
  font-size: 0.8rem;
}

h5 {
  font-size: 0.77rem;
}

small {
  font-size: 0.75rem;
}

.profile-photo {
  width: 2.8rem;
  height: 2.8rem;
  border-radius: 50%;
  overflow: hidden;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  -o-border-radius: 50%;
}

.text-muted {
  color: var(--color-info-dark);
}

p {
  color: var(--color-dark-variant);
}

b {
  color: var(--color-dark);
}

.primary {
  color: var(--color-primary);
}

.danger {
  color: var(--color-danger);
}

.success {
  color: var(--color-success);
}

.warning {
  color: var(--color-warning);
}

aside {
  height: 100vh;
}

aside .top {
  background: var(--color-background);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 1.4rem;
}

aside .logo {
  display: flex;
  gap: 0.8rem;
}

aside .logo img {
  border-radius: var(--card-border-radius);
  width: 2rem;
  height: 2rem;
  -webkit-border-radius: var(--card-border-radius);
  -moz-border-radius: var(--card-border-radius);
  -ms-border-radius: var(--card-border-radius);
  -o-border-radius: var(--card-border-radius);
}

aside .close {
  display: none;
}

aside .sidebar {
  background: var(--color-background);
  display: flex;
  flex-direction: column;
  height: 86vh;
  position: relative;
  top: 3rem;
}

aside h3 {
  font-weight: 500;
  font-weight: bold;
}

aside .sidebar a {
  display: flex;
  color: var(--color-info-dark);
  margin-left: 1rem;
  gap: 1rem;
  align-items: center;
  position: relative;
  height: 3.7rem;
  transition: all 300ms ease;
  -webkit-transition: all 300ms ease;
  -moz-transition: all 300ms ease;
  -ms-transition: all 300ms ease;
  -o-transition: all 300ms ease;
}
aside .sidebar a span {
  font-size: 1.6rem;
  transition: all 300ms ease;
}

aside .sidebar a:last-child {
  position: absolute;
  bottom: 2rem;
  width: 100%;
}

aside .sidebar a.active,
aside .sidebar a.logout {
  background: var(--color-light);
  color: var(--color-primary);
  margin-left: 0;
}
aside .sidebar a.active:before,
aside .sidebar a.logout:before {
  content: "";
  width: 6px;
  height: 100%;
  background: var(--color-primary);
}

aside .sidebar a.active span {
  color: var(--color-primary);
  margin-left: calc(1rem - 3px);
}

aside .sidebar a:hover {
  color: mediumvioletred;
  background: var(--color-light);
}

aside .sidebar a:hover span {
  margin-left: 0.5rem;
}

aside .sidebar .message-count {
  background: var(--color-danger);
  color: var(--color-white);
  padding: 2px 10px;
  font-size: 11px;
  border-radius: var(--border-radius-1);
  -webkit-border-radius: var(--border-radius-1);
  -moz-border-radius: var(--border-radius-1);
  -ms-border-radius: var(--border-radius-1);
  -o-border-radius: var(--border-radius-1);
}

main {
  margin-top: 1.4rem;
}

main .date {
  display: inline-block;
  background: var(--color-light);
  border-radius: var(--border-radius-1);
  margin-top: 1rem;
  padding: 0.5rem 1.6rem;
  -webkit-border-radius: var(--border-radius-1);
  -moz-border-radius: var(--border-radius-1);
  -ms-border-radius: var(--border-radius-1);
  -o-border-radius: var(--border-radius-1);
}

main .date input[type="date"] {
  background: transparent;
  color: var(--color-dark);
}

main .date input {
  background: black;
  color: var(--color-dark);
}

main .insights {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.6rem;
}

main .insights > div {
  background: var(--color-white);
  padding: var(--card-padding);
  border-radius: var(--card-border-radius);
  margin-top: 1rem;
  box-shadow: var(--box-shadow);
  transition: all 300ms ease;
  -webkit-transition: all 300ms ease;
  -moz-transition: all 300ms ease;
  -ms-transition: all 300ms ease;
  -o-transition: all 300ms ease;
  -webkit-border-radius: var(--card-border-radius);
  -moz-border-radius: var(--card-border-radius);
  -ms-border-radius: var(--card-border-radius);
  -o-border-radius: var(--card-border-radius);
}

main .insights > div:hover {
  box-shadow: none;
}

main .insights > div span {
  background: var(--color-primary);
  padding: 0.5rem;
  border-radius: 50%;
  color: var(--color-white);
  font-size: 2rem;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  -o-border-radius: 50%;
}
main .insights > div.sales span {
  background: var(--color-warning);
}

main .insights > div.expenses span {
  background: var(--color-danger);
}

main .insights > div.income span {
  background: var(--color-success);
}

main .insights > div .middle {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

main .insights h3 {
  margin: 1rem 0 0.6rem;
  font-size: 1rem;
}

main .insights .progress {
  position: relative;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  -o-border-radius: 50%;
}

main .insights svg {
  width: 7rem;
  height: 7rem;
}

main .insights svg circle {
  fill: none;
  stroke: var(--color-primary);
  stroke-width: 14;
  stroke-linecap: round;
  transform: translate(5px, 5px);
  stroke-dasharray: 110;
  stroke-dashoffset: 92;
  -webkit-transform: translate(5px, 5px);
  -moz-transform: translate(5px, 5px);
  -ms-transform: translate(5px, 5px);
  -o-transform: translate(5px, 5px);
}

main .insights .sales svg circle {
  stroke-dashoffset: -30;
  stroke-dasharray: 200;
}
main .insights .expenses svg circle {
  stroke-dashoffset: 20;
  stroke-dasharray: 80;
}

main .insights .income svg circle {
  stroke-dashoffset: -20;
  stroke-dasharray: 170;
}

main .insights .progress .number {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

main .insights small {
  margin-top: 1.6rem;
  display: block;
}

main .recent-order {
  margin-top: 2rem;
}

main .recent-order h2 {
  margin-bottom: 0.8rem;
}

main .recent-order table {
  background: var(--color-white);
  width: 100%;
  border-radius: var(--card-border-radius);
  padding: var(--card-padding);
  text-align: center;
  box-shadow: var(--box-shadow);
  transition: all 300ms ease;
  -webkit-border-radius: var(--card-border-radius);
  -moz-border-radius: var(--card-border-radius);
  -ms-border-radius: var(--card-border-radius);
  -o-border-radius: var(--card-border-radius);
}

main .recent-order table:hover {
  box-shadow: none;
}

main table tbody td {
  height: 2.8rem;
  border-bottom: 1px solid var(--color-light);
  color: var(--color-primary-variant);
}

main table tbody tr:last-child td {
  border: none;
}

main .recent-order a {
  text-align: center;
  display: block;
  margin: 1rem auto;
  color: var(--color-dark-variant);
}

.right {
  margin-top: 1.4rem;
}

.right .top {
  display: flex;
  justify-content: end;
  gap: 2rem;
}

.right .top button {
  display: none;
}

.right .theme-toggler {
  background: var(--color-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 1.6rem;
  width: 4.2rem;
  cursor: pointer;
  border-radius: var(--border-radius-1);
  -webkit-border-radius: var(--border-radius-1);
  -moz-border-radius: var(--border-radius-1);
  -ms-border-radius: var(--border-radius-1);
  -o-border-radius: var(--border-radius-1);
}

.right .theme-toggler span {
  font-size: 1.2rem;
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right .theme-toggler span.active {
  background: var(--color-primary);
  color: white;
  border-radius: var(--border-radius-1);
  -webkit-border-radius: var(--border-radius-1);
  -moz-border-radius: var(--border-radius-1);
  -ms-border-radius: var(--border-radius-1);
  -o-border-radius: var(--border-radius-1);
}

.right .top .profile {
  display: flex;
  gap: 2rem;
  text-align: right;
}

.right .recent-updates {
  margin-top: 1rem;
}

.right .recent-updates h2 {
  margin-bottom: 0.8rem;
}

.right .recent-updates .updates {
  background: var(--color-white);
  padding: var(--card-padding);
  border-radius: var(--card-border-radius);
  box-shadow: var(--box-shadow);
  transition: all 300ms ease;
  -webkit-border-radius: var(--card-border-radius);
  -moz-border-radius: var(--card-border-radius);
  -ms-border-radius: var(--card-border-radius);
  -o-border-radius: var(--card-border-radius);
  -webkit-transition: all 300ms ease;
  -moz-transition: all 300ms ease;
  -ms-transition: all 300ms ease;
  -o-transition: all 300ms ease;
}

.right .recent-updates .updates:hover {
  box-shadow: none;
}
.right .recent-updates .updates .update {
  display: grid;
  grid-template-columns: 2.6rem auto;
  gap: 1rem;
  margin-bottom: 1rem;
}

.right .sales-analytics {
  margin-top: 2rem;
}

.right .sales-analytics h2 {
  margin-bottom: 0.8rem;
}
.right .sales-analytics .item {
  background: var(--color-white);
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.7rem;
  padding: 1.4rem var(--card-padding);
  border-radius: var(--border-radius-3);
  box-shadow: var(--box-shadow);
  transition: all 300ms ease;
  -webkit-border-radius: var(--border-radius-3);
  -moz-border-radius: var(--border-radius-3);
  -ms-border-radius: var(--border-radius-3);
  -o-border-radius: var(--border-radius-3);
  -webkit-transition: all 300ms ease;
  -moz-transition: all 300ms ease;
  -ms-transition: all 300ms ease;
  -o-transition: all 300ms ease;
}

.right .sales-analytics .item:hover {
  box-shadow: none;
}

.right .sales-analytics .item .right {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin: 0;
  width: 100%;
}

.right .sales-analytics .item .icon {
  padding: 0.6rem;
  color: var(--color-white);
  border-radius: 50%;
  background: var(--color-primary);
  display: flex;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  -o-border-radius: 50%;
}

.right .sales-analytics .item.offline .icon {
  background: var(--color-danger);
}

.right .sales-analytics .add-product {
  background-color: transparent;
  border: 2px dashed var(--color-primary);
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

.right .sales-analytics .add-product:hover {
  background: var(--color-primary);
  color: var(--color-white);
}

.right .sales-analytics .add-product div {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.right .sales-analytics .add-product div h3 {
  font-weight: 600;
}

@media screen and (max-width: 1200px) {
  .container {
    width: 94%;
    grid-template-columns: 7rem auto 23rem;
  }
  aside .logo h2 {
    display: none;
  }
  aside .sidebar h3 {
    display: none;
  }

  aside .sidebar a {
    width: 5.6rem;
  }
  aside .sidebar a:last-child {
    position: relative;
    margin-top: 1.8rem;
  }

  main .insights {
    grid-template-columns: 1fr;
    gap: 0;
  }
  main .recent-order {
    width: 94%;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    margin: 2rem 0 0 8.8rem;
    -webkit-transform: translate(-50%);
    -moz-transform: translate(-50%);
    -ms-transform: translate(-50%);
    -o-transform: translate(-50%);
  }
  main .recent-order table {
    width: 83vw;
  }
  main table tbody tr th:last-child,
  main table tbody tr th:first-child {
    display: none;
  }
}

@media screen and (max-width: 768px) {
  .container {
    width: 100%;
    grid-template-columns: 1fr;
  }
  aside {
    position: fixed;
    left: -100%;
    background: var(--color-white);
    width: 18rem;
    z-index: 3;
    box-shadow: 1rem 3rem 4rem var(--box-shadow);
    height: 100vh;
    padding-right: var(--card-padding);
    display: none;
    animation: showMenu 400ms ease forwards;
    -webkit-animation: showMenu 400ms ease forwards;
  }

  @keyframes showMenu {
    to {
      left: 0;
    }
  }

  aside .logo {
    margin-left: 1rem;
  }
  aside .logo h2 {
    display: inline;
  }

  aside .sidebar h3 {
    display: inline;
  }

  aside .sidebar a {
    width: 100%;
    height: 3.4rem;
  }
  aside .sidebar a:last-child {
    position: absolute;
    bottom: 5rem;
  }

  aside .close {
    display: inline-block;
    cursor: pointer;
  }
  main {
    margin-top: 8rem;
    padding: 0 1rem;
  }

  main .recent-order {
    position: relative;
    margin: 3rem 0 0 0;
    width: 100%;
  }
  main .recent-order table {
    width: 100%;
    margin: 0;
  }

  .right {
    width: 94%;
    margin: 0 auto 4rem;
  }

  .right .top {
    position: fixed;
    top: 0;
    left: 0;
    align-items: center;
    padding: 0 0.8rem;
    height: 4.6rem;
    background: var(--color-white);
    width: 100%;
    margin: 0;
    z-index: 2;
    box-shadow: 0 1rem var(--color-light);
  }

  .right .top .theme-toggler {
    width: 4.4rem;
    position: absolute;
    left: 66%;
  }
  .right .profile .info {
    display: none;
  }
  .right .top button {
    display: inline-block;
    background: transparent;
    cursor: pointer;
    color: var(--color-dark);
    position: absolute;
    left: 1rem;
    font-size: 2rem;
  }
  .right .top button span {
    font-size: 2rem;
  }
}

    </style>
    <title>Salazar</title>
</head>

<body>
    <div class="container">
        <aside>
            <div class="top">
                <div class="logo">
                    <img src="https://th.bing.com/th/id/OIP.3KpdO49CueH6qtNmwP3bYgHaD4?pid=ImgDet&rs=1" alt="">
                    <h2 class="text-muted">Mario
                        <span class="danger">Salazar</span>
                    </h2>
                </div>
                <div class="close" id="close-btn">
                    <span class="material-icons-sharp">
                        highlight_off
                    </span>
                </div>
            </div>
            <div class="sidebar">
                <a class="active" href="#">
                    <span class="material-icons-sharp">
                        grid_view
                    </span>
                    <h3>Dashboard</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        person
                    </span>
                    <h3>Customer</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        receipt_long
                    </span>
                    <h3>Orders</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        insights
                    </span>
                    <h3>Analytics</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        mail
                    </span>
                    <h3>Messages</h3>
                    <span class="message-count">26</span>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        inventory
                    </span>
                    <h3>Products</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        report
                    </span>
                    <h3>Reports</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        settings
                    </span>
                    <h3>Settings</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        add_circle
                    </span>
                    <h3>Add new Product</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        manage_accounts
                    </span>
                    <h3>Manage Accouts</h3>
                </a>
                <a href="#">
                    <span class="material-icons-sharp">
                        account_balance
                    </span>
                    <h3>Account Balance</h3>
                </a>
            </div>
        </aside>
        <main>
            <h1>Dashboard</h1>
            <div class="date">
                <input type="date">
            </div>
            <div class="insights">
                <div class="sales">
                    <span class="material-icons-sharp">
                        analytics
                    </span>
                    <div class="middle">
                        <div class="left">
                            <h3>Total Sales</h3>
                            <h1>$ 25,236</h1>
                        </div>
                        <div class="progress">
                            <svg>
                                <circle cx="38" cy="38" r="36"></circle>
                            </svg>
                            <div class="number">
                                <p>81 %</p>
                            </div>
                        </div>
                    </div>
                    <small class="text-muted">
                        Last 24 Hours
                    </small>
                </div>

                <div class="expenses">
                    <span class="material-icons-sharp">
                        assessment
                    </span>
                    <div class="middle">
                        <div class="left">
                            <h3>Total Expenses</h3>
                            <h1>$ 11,257</h1>
                        </div>
                        <div class="progress">
                            <svg>
                                <circle cx="38" cy="38" r="36"></circle>
                            </svg>
                            <div class="number">
                                <p>81 %</p>
                            </div>
                        </div>
                    </div>
                    <small class="text-muted">
                        Last 24 Hours
                    </small>
                </div>

                <div class="income">
                    <span class="material-icons-sharp">
                        stacked_line_chart
                    </span>
                    <div class="middle">
                        <div class="left">
                            <h3>Total Income</h3>
                            <h1>$ 22,056</h1>
                        </div>
                        <div class="progress">
                            <svg>
                                <circle cx="38" cy="38" r="36"></circle>
                            </svg>
                            <div class="number">
                                <p>81 %</p>
                            </div>
                        </div>
                    </div>
                    <small class="text-muted">
                        Last 24 Hours
                    </small>
                </div>

            </div>
            <div class="recent-order">
                <h2>Recent Order</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Product Name</th>
                            <th>Product Number</th>
                            <th>Payment</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>


                </table>
                <a href="#">Show All</a>
            </div>
        </main>
        <div class="right">
            <div class="top">
                <button id="menu-btn">
                    <span class="material-icons-sharp">menu</span>
                </button>
                <div class="theme-toggler">
                    <span class="material-icons-sharp active">light_mode</span>
                    <span class="material-icons-sharp">dark_mode</span>
                </div>
                <div class="profile">
                    <div class="info">
                        <p>Hey, <b>Mario Salazar</b></p>
                        <small class="text-muted">User Admin</small>
                    </div>
                    <div class="profile-photo">
                        <img src="https://www.shutterstock.com/image-vector/realistic-full-moon-detailed-vector-260nw-439390066.jpg" alt="">
                    </div>
                </div>
            </div>
            <div class="recent-updates">
                <h2>Recents Updates</h2>
                <div class="updates">
                    <div class="update">
                        <div class="profile-photo">
                            <img src="https://www.shutterstock.com/image-vector/realistic-full-moon-detailed-vector-260nw-439390066.jpg" alt="">
                        </div>
                        <div class="message">
                            <p><b>Mario Salazar</b> received his order of Night lion tech GPS drone</p>
                            <small class="text-muted">3 Minutes Ago</small>
                        </div>
                    </div>
                    <div class="update">
                        <div class="profile-photo">
                            <img src="https://www.shutterstock.com/image-vector/realistic-full-moon-detailed-vector-260nw-439390066.jpg" alt="">
                        </div>
                        <div class="message">
                            <p><b>María José Salazar</b> received his order of Night lion tech GPS drone</p>
                            <small class="text-muted">5 Minutes Ago</small>
                        </div>
                    </div>
                </div>
            </div>
            <div class="sales-analytics">
                <h2>Sales Analytics</h2>
                <div class="item offline">
                    <div class="icon">
                        <span class="material-icons-sharp active">local_mall</span>
                    </div>
                    <div class="right">
                        <div class="info">
                            <h3>OFFLINE ORDERS</h3>
                            <small class="text-muted">Last 24 Hours</small>
                        </div>
                        <h5 class="danger">-19 %</h5>
                        <h3>1256</h3>
                    </div>
                </div>

                <div class="item online">
                    <div class="icon">
                        <span class="material-icons-sharp active">shopping_cart</span>
                    </div>
                    <div class="right">
                        <div class="info">
                            <h3>ONLINE ORDERS</h3>
                            <small class="text-muted">Last 24 Hours</small>
                        </div>
                        <h5 class="success">+39 %</h5>
                        <h3>6212</h3>
                    </div>
                </div>

                <div class="item customers">
                    <div class="icon">
                        <span class="material-icons-sharp active">person</span>
                    </div>
                    <div class="right">
                        <div class="info">
                            <h3>NEW ORDERS</h3>
                            <small class="text-muted">Last 24 Hours</small>
                        </div>
                        <h5 class="success">+25 %</h5>
                        <h3>369</h3>
                    </div>
                </div>
                <div class="item add-product">
                    <div>
                        <span class="material-icons-sharp active">public</span>
                        <a href="https://hungry-spence-fd4538.netlify.app/">
                            <h3>Go to Social Media Dashboard</h3>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        const Orders = [
                {
                    productName: 'Foldable Mini Drone',
                    productNumber: '46499',
                    paymentStatus: 'Due',
                    shipping: 'Pending'
                },
                {
                    productName: 'Larvender KF102 Drone',
                    productNumber: '31516',
                    paymentStatus: 'Rufunded',
                    shipping: 'Declined'
                },
                {
                    productName: 'Ruko F11 Pro Done',
                    productNumber: '5265',
                    paymentStatus: 'Due',
                    shipping: 'Pending'
                },
                {
                    productName: 'Drone with Camera Drone',
                    productNumber: '3648',
                    paymentStatus: 'Paid',
                    shipping: 'Delivered'
                },
                {
                    productName: 'Foldable Mini Drone',
                    productNumber: '46499',
                    paymentStatus: 'Due',
                    shipping: 'Pending'
                }
            ]
            const sideMenu = document.querySelector("aside");
            const menuBtn = document.querySelector("#menu-btn");
            const closeBtn = document.querySelector("#close-btn");
            const themeToggler = document.querySelector(".theme-toggler");

            menuBtn.addEventListener("click", () => {
                sideMenu.style.display = "block";
            })

            closeBtn.addEventListener("click", () => {
                sideMenu.style.display = "none";
            })

            themeToggler.addEventListener("click", () => {
                document.body.classList.toggle("dark-theme-variables");

                themeToggler.querySelector("span:nth-child(1)").classList.toggle("active");
                themeToggler.querySelector("span:nth-child(2)").classList.toggle("active");
            })

            Orders.forEach(order => {
                const tr = document.createElement('tr');
                const trContent = ` 
                        <td>${order.productName}</td>
                        <td>${order.productNumber}</td>
                        <td>${order.paymentStatus}</td>
                        <td class="${order.shipping === 'Declined' ? 'danger' :
                        order.shipping === 'Pending' ? 'warning' :
                            order.shipping === 'Delivered' ? 'success' : 'primary'}">${order.shipping}</td>
                        <td class="primary">Details</td>
                        `;
                tr.innerHTML = trContent;
                document.querySelector("table tbody").appendChild(tr);

            });
            
    </script>
    
</body>

</html>
            """


if __name__ == '__main__':
    app.run()