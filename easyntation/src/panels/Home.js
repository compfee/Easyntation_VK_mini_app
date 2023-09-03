import React from 'react';
import PropTypes from 'prop-types';

import {
	Panel,
	PanelHeader,
	Header,
	Button,
	Group,
	Cell,
	Div,
	Avatar,
	FormItem,
	File,
	View,
	Progress
} from '@vkontakte/vkui';
import {Icon24Camera, Icon24Document} from "@vkontakte/icons";

async function generate_annotation(){
	let annotation = await eel.parse_annotation_py(doc_name = 'C:/Users/compf/Documents/Diploma/data/НИР_ВласенкоНА.pdf', annot_page_number = 1)
}
// document.getElementById("btn-annot").onclick = create_cur_for_rub;

const Home = ({ id, go, fetchedUser }) => (
	<View activePanel="panel">
		<Panel id="panel">
			<PanelHeader>Easyntation</PanelHeader>
			<Group>
				<FormItem top="Загрузите документ">
					<File before={<Icon24Document role="presentation" />} size="l" mode="secondary" />
				</FormItem>
				<Div>
					<Button size="xl" level="2" onClick={generate_annotation}>
						Сгенерировать
					</Button>
				</Div>
				<FormItem>
					TODO:сделать так чтобы прибавлялось
					<Progress aria-labelledby="progresslabel" value={null} />
				</FormItem>
			</Group>
		</Panel>

	</View>
)
Home.propTypes = {
	id: PropTypes.string.isRequired,
	go: PropTypes.func.isRequired,
	fetchedUser: PropTypes.shape({
		photo_200: PropTypes.string,
		first_name: PropTypes.string,
		last_name: PropTypes.string,
		city: PropTypes.shape({
			title: PropTypes.string,
		}),
	}),
};

export default Home;
